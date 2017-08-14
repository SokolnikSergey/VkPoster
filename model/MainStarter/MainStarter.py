from PyQt5.QtCore import pyqtSignal,QObject
from model.ConfigParser.ConfigParserPostToGroup.ConfigParserPostToGroup import ConfigParser
from model.ConfigParser.ConfigContainerPostToGroup.ConfigContainerPostToGroup import ConfigContainerPostToGroup
from model.SplashScreen.SplashScreen import SplashScreen
from model.VkSessionData.VkSessionData import VkSessionData
from model.VkSessionData.VkSessionDataConfigurator import VkSessionDataConfigurator
from model.Messages.AcceptLeaveApp import AcceptLeaveApp
from model.VkAuthorizationModel.VkAuthorizationModel import VkAuthorizationModel
from view.StartChoice.StartChoiceViewOperator import  StartChoiceViewOperator
from view.StartChoice.StartChoiceWindow import StartChoiceWindow
from model.MainStarter.Binder import StartChoiceBinder
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
import sys,shelve,os
from PyQt5.QtWidgets import QApplication

class MainStarter(QObject):
    change_account = pyqtSignal()
    post_to_group_pressed = pyqtSignal()
    setting_pressed  = pyqtSignal()

    def __init__(self,logger):
        super(MainStarter, self).__init__()


        self.__logger  = logger

        self.create_splash_screen()
        self.__splash_screen.show()
        self.create_auxiliary_elements()
        self.show()
        self.check_token_on_start()
        self.__splash_screen.hide()

    def accept_exit(self):
        if self.__accept_leave_app.exec() == AcceptLeaveApp.Ok:
            return True
        return False

    def create_messages_and_warnings(self):
        self.__accept_leave_app = AcceptLeaveApp()

    def show(self):
        self.__start_choice_win_operator.show()

    def hide(self):
        self.__start_choice_win_operator.hide()

    def create_binder(self):
        self.binder = StartChoiceBinder(self.__start_choice_win_operator,self)

    def create_view(self):
        self.__start_choice_win_operator = StartChoiceViewOperator(StartChoiceWindow())

    def create_splash_screen(self):
        self.__splash_screen = SplashScreen("../AuxElements/hqdefault.jpg")

    def create_vk_authhorization(self):
        self.__vk_authorization_model = VkAuthorizationModel(self.__config_container.application_id)

    def snapping_signals(self):
        self.__vk_authorization_model.token_recieved_signal.connect \
            (self.__vk_session_data_configurator.update_session_data_container_with_new_token)
        self.__vk_authorization_model.token_recieved_signal.connect(self.__vk_authorization_model.hide)
        self.__vk_authorization_model.auth_window_closed.connect(self.__vk_authorization_model.hide)
        self.__vk_authorization_model.auth_window_closed.connect(self.check_existing_of_token)
        self.__vk_operator.action_has_done.connect(self.__leisurely_queue_executor.last_action_has_executed)
        self.__settings_model.update_settings.connect(self.__config_parser_vk_operations.update_values)
        self.__post_to_group_model.btn_helper_clecked.connect(self.start_hepler)



    def start_hepler(self):
        try :
            os.startfile("..\AuxElements\Helper.chm")

        except Exception as ex:
            logger.change_name(self.__class__.__name__)
            logger.exception(ex)


    def check_token_on_start(self):
        token = self.__vk_session_data.token
        if not token:
            self.get_token()

    def check_existing_of_token(self):
        token = self.__vk_session_data.token
        if not token:
            if self.accept_exit():
                app.exit()
            else:
                self.get_token()

    def get_token(self):
        self.__vk_authorization_model.show()
        self.__vk_authorization_model.start_authorization()
###############################################################

    def create_auxiliary_elements(self):
        self.__handlder_ex = ExceptionHandler()

        self.create_config_container()
        self.create_config_parser()
        self.create_settings_manager()

        self.create_vk_session_data()
        self.create_vk_session_data_configurator(self.__vk_session_data)
        self.create_messages_and_warnings()
        self.create_containers()
        self.create_action_executors(self.__vk_session_data)
        self.create_models()
        self.create_exceptions()
        self.create_liable_about_view()
        self.create_view()
        self.create_action_binder()
        self.create_binder()
        self.snapping_signals()
        self.create_and_bind_handlers()

        self.__logger.info("APP successfully started!")

    def create_settings_manager(self):
        self.__settings_manager = SettingsManager(self.__config_container_vk_operations)

    def create_exceptions(self):
        self.__warning_message = ExceptionWarning("")

    def create_and_bind_handlers(self):
        self.__ex_signals_binder = ExceptionSignalsBinder\
            (self.__handlder_ex,self.__post_to_group_model,self.__edit_post_model,
             self.__liable_about_view,self.__warning_message)

    def create_models(self):
        self.create_settings_model()
        self.create_post_to_group()
        self.create_chose_post_for_edit()
        self.create_edit_post_model()
        self.create_vk_authhorization()

    def create_settings_model(self):
        print((self.__config_container_vk_operations.country_number,
                                  self.__config_container_vk_operations.max_amount_of_groups,
                                  self.__config_container_vk_operations.min_amount_users_in_group,
                                  self.__config_container_vk_operations.timeout,
                                  self.__config_container_vk_operations.each_to_each))
        self.__settings_model = SettingsModel(self.__config_container_vk_operations.country_number,
                                  self.__config_container_vk_operations.max_amount_of_groups,
                                  self.__config_container_vk_operations.min_amount_users_in_group,
                                  self.__config_container_vk_operations.timeout,
                                  self.__config_container_vk_operations.each_to_each)

    def create_post_to_group(self):
        self.__post_to_group_model = PostToGroupModel(PostContainerWithQImages([]),
                                                      GroupContainerWithQImages([]), self.__post_container,
                                                      self.__group_container)
        self.__post_to_group_model.subscribe_to_leisurely_executor(self.__leisurely_queue_executor)

    def create_chose_post_for_edit(self):
        self.__chose_post_for_edit = ChosePostForEditModel(PostContainerWithQImages([]),
                                                           self.__post_container)

    def create_edit_post_model(self):
        self.__edit_post_model = EditPostModel()

    def create_action_executors(self,session_data):
        self.__vk_operator = VkOperator(self.__logger,self.__vk_session_data,self.__group_container,
        session_data.vk_api,PhotoManager(self.__logger,self.__config_container.photo_complience_path,
                            self.__vk_session_data,PhotoCompliancesContainer([],[])))

        self.__action_executor = ActionExecutor(self.__vk_operator,StorageOperator(self.__logger,
                    self.__post_container,shelve.open(self.__config_container.post_container_path)))

        self.__hurriedly_queue_executor = HurriedlyQueueExecutor(
            self.__actions_queue,[],self.__action_executor)

        self.__leisurely_queue_executor = LeisurelyQueueExecutor(
            self.__actions_queue, [], self.__action_executor)

        self.__edit_container_queue_executor = EditContainersQueueExecutor(
            self.__actions_queue, [], self.__action_executor)

    def create_containers(self):
        self.__post_container = PostContainer([])
        self.__group_container = GroupContainer([])
        self.__actions_queue = ActionQueue([],[],[])

    def create_action_binder(self):
        self.__action_binder = ActionBinder(self.__post_to_group_model,self.__chose_post_for_edit,
                                            self.__edit_post_model,ActionMaker(self.__actions_queue,5,0,0))

    def create_liable_about_view(self):
        self.__liable_about_view = LiableAboutView(self.__settings_model, self,
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
    starter = MainStarter(logger)
except Exception as ex:
    logger.exception(ex)
sys.exit(app.exec_())

