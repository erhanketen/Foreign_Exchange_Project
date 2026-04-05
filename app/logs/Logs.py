import datetime
import Log_funcs as lgf

""" LOGS CLASS """

class Logs:
    def __init__(self,log_user_id,action):
        self.log_id = lgf.generate_log_id()
        self.log_user_id = log_user_id
        self.logged_at = datetime.datetime.now()
        self.action = action

    def get_log_info(self):
        return [self.log_id,self.log_user_id,self.logged_at,self.action]

