from PyQt5.QtCore import QObject
from model.ConfigParser.ConfigParserPostToGroup.ConfigParserPostToGroup import ConfigParser
from model.ActionsDelayer.ActionDelayer import ActionDelayer
from model.ConfigParser.ConfigContainerPostToGroup.ConfigContainerPostToGroup import ConfigContainerPostToGroup
from model.SplashScreen.SplashScreen import SplashScreen
from model.VkSessionData.VkSessionData import VkSessionData
from model.VkSessionData.VkSessionDataConfigurator import VkSessionDataConfigurator
from model.Messages.AcceptLeaveApp import AcceptLeaveApp
from model.VkAuthorizationModel.VkAuthorizationModel import VkAuthorizationModel
from model.StartChoiceModel.StartChoiceModel import StartChoiceModel
from model.LiableAboutView.LiableAboutView import LiableAboutView
from model.ChosePostForEdit.ChosePostForEditModel import ChosePostForEditModel
from model.PostToGroup.PostToGroupModel import PostToGroupModel
from model.EditPost.EditPostModel import EditPostModel
from model.ExceptionHandler.ExceptionHandler import ExceptionHandler
from model.ExceptionSignalsBinder.ExceptionSignalsBinder import ExceptionSignalsBinder
from view.Exceptions.ExceptionWarning import ExceptionWarning
from model.ActionBinder import ActionBinder
from model.ActionExecturors.ActionExecutor import ActionExecutor
from model.ActionExecturors.EditContainersQueueExecutor import EditContainersQueueExecutor
from model.ActionExecturors.HurriedlyQueueExecutor import HurriedlyQueueExecutor
from model.ActionExecturors.LeisurelyQueueExecutor import LeisurelyQueueExecutor
from model.ActionExecturors.VkOperator import VkOperator
from model.ActionMaker.ActionMaker import ActionMaker
from model.Containers.ActionQueue.ActionQueue import ActionQueue
from model.Containers.GroupContainer.GroupContainer import GroupContainer
from model.Containers.GroupContainer.GroupContainerWithQImages import GroupContainerWithQImages
from model.Containers.PostContainer.PostContainer import PostContainer
from model.Containers.PostContainer.PostContainerWithQImages import PostContainerWithQImages
from model.PhotoManager.PhotoManager import PhotoManager
from model.StorageOperator.StorageOperator import StorageOperator
from model.Containers.PhotoCompliancesContainer import PhotoCompliancesContainer
from model.ConfigParser.ConfigContainerPostToGroup.ConfigContainerVkOpererations import ConfigContainerVkOperations
from model.ConfigParser.ConfigParserPostToGroup.ConfigParserVkOperGathering import ConfigParserVkOperationGathering
from model.SettingsManager.SettingsManager import SettingsManager
from model.Settings.SettingsModel import SettingsModel
from model.Logger.Logger import MyLogger
from model.ProgressBinder.ProgressBinder import ProgressBinder
from model.Containers.SendingsContainer import SendingsContainer
import sys,shelve,os, subprocess

from datetime import datetime


from PyQt5.QtWidgets import QApplication

class MainStarter(QObject):

    def __init__(self,logger, app):
        super(MainStarter, self).__init__()
        self.__start_timestamp = str(int(datetime.timestamp(datetime.now())))
        self.save_start_timestamp()

        self.create_splash_screen()
        self.__splash_screen.show()

        for i in range(10_000):  # Need to show splash -> dirty hack from stack overflow ) but it works as expected !
            app.processEvents()

        self.__logger = logger
        self.__action_maker = None
        self.create_auxiliary_elements()
        self.__start_choice_model.show()
        self.__splash_screen.hide()

        self.create_messages_and_warnings()
        self.check_existing_of_token()

    def accept_exit(self):
        if self.__accept_leave_app.exec() == AcceptLeaveApp.Ok:
            return False
        return True

    def create_messages_and_warnings(self):
        self.__accept_leave_app = AcceptLeaveApp()

    def snapping_signals(self):
        self.__vk_authorization_model.token_recieved_signal.connect \
            (self.__vk_session_data_configurator.update_session_data_container_with_new_token)
        self.__vk_authorization_model.token_recieved_signal.connect(self.__vk_authorization_model.hide)
        self.__vk_authorization_model.auth_window_closed.connect(self.__vk_authorization_model.hide)
        self.__vk_authorization_model.auth_window_closed.connect(self.check_existing_of_token)
        self.__vk_operator.action_has_done.connect(self.__leisurely_queue_executor.last_action_has_executed)
        self.__vk_operator.action_has_done.connect(self.__leisurely_queue_executor.increment_action_has_done)
        self.__vk_operator.action_has_done.connect(self.__leisurely_queue_executor.notify_suscribers_about_changes_of_amount)
        self.__vk_operator.action_has_failed.connect(self.__leisurely_queue_executor.increment_action_has_failed)
        self.__vk_operator.action_has_failed.connect(
            self.__leisurely_queue_executor.notify_suscribers_about_changes_of_amount)
        self.__vk_operator.action_has_failed.connect(self.__leisurely_queue_executor.last_action_has_executed)
        self.__settings_model.update_settings.connect(self.__config_parser_vk_operations.update_values)
        self.__start_choice_model.change_account.connect(self.get_token)
        self.__vk_operator.actions_delayed.connect(self.__action_delayer.write_all_action_to_file)
        self.__post_to_group_model.recover_actions_clicked.connect(self.__action_delayer.read_actions_from_file)
        self.__post_to_group_model.btn_helper_clecked.connect(self.start_helper)

        self.__vk_operator.uploaded_thread.need_to_upload_photos.connect(self.__post_to_group_model.show_start_upload_image)
        self.__vk_operator.uploaded_thread.data_have_uploaded_to_vk.connect(self.__post_to_group_model.hide_start_upload_image)

    def start_helper(self):
        if sys.platform == "win32":
            os.startfile("../AuxElements/Helper.chm")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "../AuxElements/Helper.chm"])

    def inform_relogin_if_user_blocked(self, vk_api):
        try:
            vk_api.users.account.getInfo(v="5.73")
        except Exception as ex:
            if str(ex).split(".")[0] == '5':
                self.__accept_leave_app.set_texts("The account is blocked by VK", "Start another authorization?")
                self.show_get_token_or_exit()

    def check_existing_of_token(self):
        self.inform_relogin_if_user_blocked(self.__vk_session_data.vk_api)
        token = self.__vk_session_data.token
        if not token:
            self.__accept_leave_app.set_texts("Application doesn't work without signed in account", "Start authorization?")
            self.show_get_token_or_exit()

    def get_token(self):
        self.__vk_authorization_model.show()
        self.__vk_authorization_model.start_authorization()

    def show_get_token_or_exit(self):
        if self.accept_exit():
            sys.exit()
        else:
            self.get_token()
###############################################################

    def save_start_timestamp(self):
        with open('../AuxElements/start_timestamp', 'w') as f:
            f.write(self.__start_timestamp)

    def create_auxiliary_elements(self):
        self.__handlder_ex = ExceptionHandler()

        self.create_config_container()
        self.create_config_parser()
        self.create_settings_manager()

        self.create_vk_session_data()
        self.create_vk_session_data_configurator(self.__vk_session_data)
        self.create_containers()
        self.create_action_executors(self.__vk_session_data)
        self.create_models()
        self.create_exceptions()
        self.create_liable_about_view()
        self.create_action_binder()
        self.create_progress_binders()
        self.create_action_delayer()
        self.snapping_signals()
        self.create_and_bind_handlers()

        self.__logger.info("APP successfully started!")

    def create_progress_binders(self):
        self.__progress_binder = ProgressBinder(self.__start_choice_model,self.__post_to_group_model,
                                                self.__leisurely_queue_executor)

    def create_splash_screen(self):
        self.__splash_screen = SplashScreen("../AuxElements/hqdefault.jpg")

    def create_vk_authhorization(self):
        self.__vk_authorization_model = VkAuthorizationModel(self.__config_container.application_id)

    def create_settings_manager(self):
        self.__settings_manager = SettingsManager(self.__config_container_vk_operations)

    def create_exceptions(self):
        self.__warning_message = ExceptionWarning("")

    def create_and_bind_handlers(self):
        self.__ex_signals_binder = ExceptionSignalsBinder\
            (self.__handlder_ex,self.__post_to_group_model, self.__chose_post_for_edit,self.__edit_post_model,
             self.__liable_about_view,self.__warning_message,self.__vk_operator)

    def create_action_delayer(self):
        self.__action_delayer = ActionDelayer(self.__actions_queue)

    def create_models(self):

        self.create_start_choice_model()
        self.create_settings_model()
        self.create_post_to_group()
        self.create_chose_post_for_edit()
        self.create_edit_post_model()
        self.create_vk_authhorization()

    def create_start_choice_model(self):
        self.__start_choice_model  = StartChoiceModel(self.__logger,self.__vk_session_data)

    def create_settings_model(self):
        self.__settings_model = SettingsModel(self.__config_container_vk_operations.country_number,
                                  self.__config_container_vk_operations.max_amount_of_groups,
                                  self.__config_container_vk_operations.min_amount_users_in_group,
                                  self.__config_container_vk_operations.timeout,
                                  self.__config_container_vk_operations.each_to_each)

    def create_post_to_group(self):
        self.__post_to_group_model = PostToGroupModel(PostContainerWithQImages([]),
                                GroupContainerWithQImages([]), self.__post_container,self.__group_container,
                              self.__sending_container, self.__photo_manager.compliances_container, self.__action_maker)

    def create_chose_post_for_edit(self):
        self.__chose_post_for_edit = ChosePostForEditModel(PostContainerWithQImages([]),
                                                           self.__post_container)

    def create_edit_post_model(self):
        self.__edit_post_model = EditPostModel()

    def create_action_executors(self,session_data):
        self.__photo_manager = PhotoManager(self.__logger,self.__config_container.photo_complience_path,
                            self.__vk_session_data,PhotoCompliancesContainer([],[]),session_data.album_id )

        self.__vk_operator = VkOperator(self.__logger,self.__vk_session_data,self.__group_container,
        session_data.vk_api,self.__photo_manager,self.__sending_container )

        self.__action_executor = ActionExecutor(self.__vk_operator,StorageOperator(self.__logger,
                    self.__post_container,shelve.open(self.__config_container.post_container_path)))

        self.__hurriedly_queue_executor = HurriedlyQueueExecutor(
            self.__actions_queue,[],self.__action_executor)

        self.__leisurely_queue_executor = LeisurelyQueueExecutor(
            self.__actions_queue, [], self.__action_executor)

        self.__edit_container_queue_executor = EditContainersQueueExecutor(
            self.__actions_queue, [], self.__action_executor)

    def create_containers(self):

        self.__sending_container = SendingsContainer(current_file_timestamp=self.__start_timestamp)
        self.__post_container = PostContainer([])
        self.__group_container = GroupContainer([])
        self.__actions_queue = ActionQueue([],[],[])

    def create_action_binder(self):
        self.__action_maker = ActionMaker(self.__actions_queue,5,0,0)
        self.__post_to_group_model.action_maker = self.__action_maker # dirty hack :(
        self.__action_binder = ActionBinder(self.__post_to_group_model,self.__chose_post_for_edit,
                                            self.__edit_post_model,self.__action_maker)

    def create_liable_about_view(self):
        self.__liable_about_view = LiableAboutView(self.__settings_model, self.__start_choice_model,
                                    self.__post_to_group_model,self.__chose_post_for_edit,
                                            self.__edit_post_model,self.__warning_message)

    def create_config_container(self):
        self.__config_container = ConfigContainerPostToGroup()
        self.__config_container_vk_operations = ConfigContainerVkOperations()

    def create_config_parser(self):
        self.__config_parser = ConfigParser("../AuxElements/in.ini", self.__config_container)
        self.__config_parser_vk_operations = ConfigParserVkOperationGathering("../AuxElements/vk_settings.ini",
                                                                self.__config_container_vk_operations)

    def create_vk_session_data(self):
        self.__vk_session_data = VkSessionData()

    def create_vk_session_data_configurator(self, session_data_container):
        self.__vk_session_data_configurator = VkSessionDataConfigurator(self.__logger,session_data_container
                                                                        , "../AuxElements/token.bin")


app = QApplication(sys.argv)
MyLogger.PATH_TO_FILE = '../AuxElements/logger'
logger = MyLogger()
try:
    starter = MainStarter(logger, app)
except Exception as ex:
    logger.exception(ex)
sys.exit(app.exec_())

