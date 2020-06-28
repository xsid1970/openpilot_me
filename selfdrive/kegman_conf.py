import json
import os

class kegman_conf():
  def __init__(self, CP=None):
    self.conf = self.read_config()
    if CP is not None:
      self.init_config(CP)

  def init_config(self, CP):
    write_conf = False
    if self.conf['tuneGernby'] != "1":
      self.conf['tuneGernby'] = str(1)
      write_conf = True
	
    # only fetch Kp, Ki, Kf sR and sRC from interface.py if it's a PID controlled car
    if CP.lateralTuning.which() == 'pid':
      if self.conf['Kp'] == "-1":
        self.conf['Kp'] = str(round(CP.lateralTuning.pid.kpV[0],3))
        write_conf = True
      if self.conf['Ki'] == "-1":
        self.conf['Ki'] = str(round(CP.lateralTuning.pid.kiV[0],3))
        write_conf = True
      if self.conf['Kf'] == "-1":
        self.conf['Kf'] = str('{:f}'.format(CP.lateralTuning.pid.kf))
        write_conf = True
      if self.conf['Kp2'] == "-1":
        self.conf['Kp2'] = str(round(CP.lateralTuning.pid.kpV[0],3))
        write_conf = True
      if self.conf['Ki2'] == "-1":
        self.conf['Ki2'] = str(round(CP.lateralTuning.pid.kiV[0],3))
        write_conf = True
      if self.conf['Kf2'] == "-1":
        self.conf['Kf2'] = str('{:f}'.format(CP.lateralTuning.pid.kf))
        write_conf = True
    
    if self.conf['steerRatio'] == "-1":
      self.conf['steerRatio'] = str(round(CP.steerRatio,3))
      write_conf = True
    
    if self.conf['steerRateCost'] == "-1":
      self.conf['steerRateCost'] = str(round(CP.steerRateCost,3))
      write_conf = True

    if write_conf:
      self.write_config(self.config)

  def read_config(self):
    self.element_updated = False

    if os.path.isfile('/data/kegman.json'):
      with open('/data/kegman.json', 'r') as f:
        self.config = json.load(f)

      if "battPercOff" not in self.config:
        self.config.update({"battPercOff":"100"})
        self.config.update({"carVoltageMinEonShutdown":"11800"})
        self.element_updated = True

      if "tuneGernby" not in self.config:
        self.config.update({"tuneGernby":"1"})
        self.config.update({"deadzone":"0.0"})

      if "Kp" not in self.config:
        self.config.update({"Kp":"-1"})
        self.config.update({"Ki":"-1"})
        self.config.update({"Kf":"-1"})
        self.element_updated = True

      if "Kp2" not in self.config:
        self.config.update({"Kp2":"-1"})
        self.config.update({"Ki2":"-1"})
        self.config.update({"Kf2":"-1"})
        self.element_updated = True

      if "steerRatio" not in self.config:
        self.config.update({"steerRatio":"-1"})
        self.config.update({"steerRateCost":"-1"})
        self.element_updated = True

      if "steerMax" not in self.config:
        self.config.update({"steerMax":"255"})
        self.element_updated = True
		
      if "sR_boost" not in self.config:
        self.config.update({"sR_boost":"0"})
        self.config.update({"sR_BP0":"0"})
        self.config.update({"sR_BP1":"0"})
        self.config.update({"sR_time":"1"})
        self.element_updated = True
      
      if "ALCnudgeLess" not in self.config:
        self.config.update({"ALCnudgeLess":"0"})
        self.element_updated = True

      if "sR_Kp" not in self.config:
        self.config.update({"sR_Kp":"0.10"})
        self.config.update({"sR_Ki":"0.01"})
        self.config.update({"sR_Kf":"0.00001"})
        self.element_updated = True

      if "sR_Kp2" not in self.config:
        self.config.update({"sR_Kp2":"0.10"})
        self.config.update({"sR_Ki2":"0.01"})
        self.config.update({"sR_Kf2":"0.00001"})
        self.element_updated = True

      if "cV_Ratio" not in self.config:
        self.config.update({"cV_Ratio":"0.7"})
        self.element_updated = True

      if "cV_Dist" not in self.config:
        self.config.update({"cV_Dist":"-5"})
        self.element_updated = True

      if "steerTorqueOver" not in self.config:
        self.config.update({"steerTorqueOver":"200"})
        self.element_updated = True

      if "ALCtimer" not in self.config:
        self.config.update({"ALCtimer":"1.0"})
        self.element_updated = True

      if "deltaUp" not in self.config:
        self.config.update({"deltaUp":"3"})
        self.element_updated = True

      if "deltaDown" not in self.config:
        self.config.update({"deltaDown":"5"})
        self.element_updated = True

      if "threshold" not in self.config:
        self.config.update({"threshold":"150"})
        self.element_updated = True

      if "leanStVelocity" not in self.config:
        self.config.update({"leanStVelocity":"40"})
        self.config.update({"leanLeftAmount":"0"})
        self.config.update({"leanRightAmount":"0"})
        self.element_updated = True



      if self.element_updated:
        print("updated")
        self.write_config(self.config)

    else:
      self.config = {"cameraOffset":"0.06", "battChargeMin":"70", "battChargeMax":"80", \
                    "wheelTouchSeconds":"30000", "battPercOff":"10", "carVoltageMinEonShutdown":"11800", \
                    "tuneGernby":"1", "deadzone":"10.0", "steerMax":"255", \
                    "cv_Ratio":"0.7", "cv_Dist":"-5", "steerTorqueOver":"200", \
                    "Kp":"-1", "Ki":"-1", "Kf":"-1", \
                    "Kp2":"-1", "Ki2":"-1", "Kf2":"-1", \
                    "deltaUp":"3", "deltaDown":"5", "threshold":"150", \
                    "leanStVelocity":"40", "leanLeftAmount":"0", "leanRightAmount":"0", \
                    "steerRatio":"-1", "steerRateCost":"-1", "ALCnudgeLess":"0", "ALCtimer":"1.0", \
                    "sR_boost":"0", "sR_BP0":"0", "sR_BP1":"0", "sR_time":"1", \
                    "sR_Kp":"0.10", "sR_Ki":"0.01", "sR_Kf":"0.00001", \
                    "sR_Kp2":"0.10", "sR_Ki2":"0.01", "sR_Kf2":"0.00001"}


      self.write_config(self.config)
    return self.config

  def write_config(self, config):
    try:
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
    except IOError:
      os.mkdir('/data')
      with open('/data/kegman.json', 'w') as f:
        json.dump(self.config, f, indent=2, sort_keys=True)
        os.chmod("/data/kegman.json", 0o764)
