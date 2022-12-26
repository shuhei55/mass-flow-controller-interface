import MassFlowController as mfc
import time

if __name__ == "__main__":
  # 通信を確立
  #mfc_obj = mfc.MFC(port="COM7", baudrate=4800, dummy=True) dummyがTrueだとつながって無くてもエラーをはかずに動く
  mfc_obj = mfc.MFC(port="COM7", baudrate=4800, dummy=False)
  # データ通信を開始
  mfc_obj.run_communication()
  # ターゲット値を指定
  mfc_obj.set_target(target_list=[0, 100, 255])
  time.sleep(2)
  # 現在の流量を確認
  print(mfc_obj.get_current_flow_list())
  # ゼロに指定
  mfc_obj.set_target(target_list=[0, 0, 0])
  # 通信を終了
  mfc_obj.stop_communication()