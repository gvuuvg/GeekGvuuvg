# 导入SmsClient配置文件
import sms_sample_conf

# 导入SMS相关模块
import sms_sample_conf
import baidubce.services.sms.sms_client as sms
import baidubce.exception as ex

# 新建SmsClient
sms_client = sms.SmsClient(sms_sample_conf.config)


def sendMsg():
    # AK  d710501823fd4762ae29203beb4772e4
    # SK  4f947922b6a848ba89b883523c66f1dc
    try:
        response = sms_client.send_message(signature_id='sms-sign-WWejWQ54455', template_id='sms-tmpl-wHoJXL09355',
                                           mobile='18088616887', content_var_dict={'content': "测试发送短信"})
    except ex.BceHttpClientError as e:
        if isinstance(e.last_error, ex.BceServerError):
            # LOG.error('send request failed. Response %s, code: %s, request_id: %s'
            #           % (e.last_error.status_code, e.last_error.code, e.last_error.request_id))
            print('send request failed. Response %s, code: %s, request_id: %s'
                  % (e.last_error.status_code, e.last_error.code, e.last_error.request_id))
        else:
            # LOG.error('send request failed. Unknown exception: %s' % e)
            print('send request failed. Unknown exception: %s' % e)


sendMsg()
