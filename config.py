default_sketch = "void setup() {\n    // Предустановка. Выполняется один раз\n\n}\n\nvoid loop() {\n    // Основной цикл программы\n\n}"
code_font = ("Cascadia code", 13)
console_font = ("Cascadia code", 13)
use_auto_check_boards = False
use_auto_check_progs = False

# if use_auto_check_boards = False
boards_ = {'Adafruit Circuit Playground': 'arduino:avr:circuitplay32u4cat', 'Arduino BT': 'arduino:avr:bt', 'Arduino Duemilanove or Diecimila': 'arduino:avr:diecimila', 'Arduino Esplora': 'arduino:avr:esplora', 'Arduino Ethernet': 'arduino:avr:ethernet', 'Arduino Fio': 'arduino:avr:fio', 'Arduino Gemma': 'arduino:avr:gemma', 'Arduino Industrial 101': 'arduino:avr:chiwawa', 'Arduino Leonardo': 'arduino:avr:leonardo', 'Arduino Leonardo ETH': 'arduino:avr:leonardoeth', 'Arduino Mega ADK': 'arduino:avr:megaADK', 'Arduino Mega or Mega 2560': 'arduino:avr:mega', 'Arduino Micro': 'arduino:avr:micro', 'Arduino Mini': 'arduino:avr:mini', 'Arduino NG or older': 'arduino:avr:atmegang', 'Arduino Nano': 'arduino:avr:nano', 'Arduino Nano ESP32': 'arduino:esp32:nano_nora', 'Arduino Pro or Pro Mini': 'arduino:avr:pro', 'Arduino Robot Control': 'arduino:avr:robotControl', 'Arduino Robot Motor': 'arduino:avr:robotMotor', 'Arduino Uno': 'arduino:avr:uno', 'Arduino Uno Mini': 'arduino:avr:unomini', 'Arduino Uno WiFi': 'arduino:avr:unowifi', 'Arduino Yún': 'arduino:avr:yun', 'Arduino Yún Mini': 'arduino:avr:yunmini', 'LilyPad Arduino': 'arduino:avr:lilypad', 'LilyPad Arduino USB': 'arduino:avr:LilyPadUSB', 'Linino One': 'arduino:avr:one'}
# if use_auto_check_progs = False
progs_ = ['2232hio', '4232h', 'adafruit_gemma', 'arduino', 'arduino-ft232r', 'diecimila', 'arduino_as_isp', 'arduino_gemma', 'arduinoisp', 'arduinoisporg', 'atmelice', 'atmelice_jtag', 'atmelice_dw', 'atmelice_isp', 'atmelice_pdi', 'atmelice_tpi', 'atmelice_updi', 'avr109', 'avr911', 'avr910', 'avrftdi', '2232h', 'avrisp', 'avrisp-u', 'avrispmkII', 'avrisp2', 'avrispv2', 'buspirate', 'buspirate_bb', 'butterfly', 'butterfly_mk', 'mkbutterfly', 'bwmega', 'c232hm', 'c2n232i', 'ch341a', 'dasa', 'dasa3', 'digilent-hs2', 'dragon_dw', 'dragon_hvsp', 'dragon_isp', 'dragon_jtag', 'dragon_pdi', 'dragon_pp', 'dryboot', 'dryrun', 'ehajo-isp', 'flip1', 'flip2', 'flyswatter2', 'ft2232h', 'ft2232h_jtag', 'ft232h', 'ft232h_jtag', 'ft232r', 'ft245r', 'ft4232h', 'iseavrprog', 'jtag1slow', 'jtag2dw', 'jtag2fast', 'jtag2', 'jtag2isp', 'jtag2pdi', 'jtag2slow', 'jtag2updi', 'nanoevery', 'jtag3', 'jtag3dw', 'jtag3isp', 'jtag3pdi', 'jtag3updi', 'jtagkey', 'jtagmkI', 'jtag1', 'jtagmkII', 'jtagmkII_avr32', 'jtag2avr32', 'ktlink', 'lm3s811', 'mib510', 'micronucleus', 'nibobee', 'o-link', 'openmoko', 'pavr', 'pickit2', 'pickit4', 'pickit4_jtag', 'pickit4_isp', 'pickit4_pdi', 'pickit4_tpi', 'pickit4_updi', 'pickit5_updi', 'pkobn_updi', 'ponyser', 'powerdebugger', 'powerdebugger_jtag', 'powerdebugger_dw', 'powerdebugger_isp', 'powerdebugger_pdi', 'powerdebugger_tpi', 'powerdebugger_updi', 'serialupdi', 'serprog', 'siprog', 'snap', 'snap_jtag', 'snap_isp', 'snap_pdi', 'snap_tpi', 'snap_updi', 'stk500', 'stk500hvsp', 'scratchmonkey_hvsp', 'stk500pp', 'scratchmonkey_pp', 'stk500v1', 'stk500v2', 'scratchmonkey', 'stk600', 'stk600hvsp', 'stk600pp', 'tc2030', 'teensy', 'tigard', 'ttl232r', 'tumpa', 'tumpa-b', 'tumpa_jtag', 'um232h', 'uncompatino', 'urclock', 'usbasp', 'usbasp-clone', 'usbtiny', 'wiring', 'xbee', 'xplainedmini', 'xplainedmini_isp', 'xplainedmini_dw', 'xplainedmini_tpi', 'xplainedmini_updi', 'xplainedpro', 'xplainedpro_jtag', 'xplainedpro_pdi', 'xplainedpro_updi']