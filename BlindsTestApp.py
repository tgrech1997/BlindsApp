
# -*- coding: utf8 -*-

import remi.gui as gui
from remi.gui import *
from remi import start, App
import BlindsModule as BM

class CLASSbtRST( Button ):
    def __init__(self, *args):
        super( CLASSbtRST, self ).__init__(*args)
        

class CLASSbtLP2( Button ):
    def __init__(self, *args):
        super( CLASSbtLP2, self ).__init__(*args)
        

class CLASSbtST( Button ):
    def __init__(self, *args):
        super( CLASSbtST, self ).__init__(*args)
        

class untitled(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path='./res/')

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        wid = VBox()
        wid.attributes.update({"editor_newclass":"False","editor_baseclass":"VBox","editor_constructor":"()","class":"VBox","editor_tag_type":"widget","editor_varname":"wid"})
        wid.style.update({"align-items":"center","height":"781px","overflow":"auto","top":"81px","flex-direction":"column","width":"239px","justify-content":"space-around","position":"absolute","margin":"0px","display":"flex","left":"393px"})
        btLSET = Button('LED Set (Instant)')
        btLSET.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('LED Set (Instant)')","class":"Button","editor_tag_type":"widget","editor_varname":"btLSET"})
        btLSET.style.update({"top":"20px","height":"30px","width":"120px","position":"static","overflow":"auto","margin":"0px","order":"26"})
        wid.append(btLSET,'btLSET')
        btSETT = Button('Setup triggers')
        btSETT.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Setup triggers')","class":"Button","editor_tag_type":"widget","editor_varname":"btSETT"})
        btSETT.style.update({"top":"619.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"1"})
        wid.append(btSETT,'btSETT')
        inMDES = TextInput(True,'20')
        inMDES.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'20')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inMDES","placeholder":"20"})
        inMDES.style.update({"top":"855.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"17","resize":"none"})
        wid.append(inMDES,'inMDES')
        inMDEN = TextInput(True,'5')
        inMDEN.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'5')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inMDEN","placeholder":"5"})
        inMDEN.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"19","resize":"none"})
        wid.append(inMDEN,'inMDEN')
        lbl = Label('Hello')
        lbl.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Hello')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl"})
        lbl.style.update({"top":"352.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"0"})
        wid.append(lbl,'lbl')
        inBDEL = TextInput(True,'0.000001')
        inBDEL.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'0.000001')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inBDEL","placeholder":"0.000001"})
        inBDEL.style.update({"top":"567.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"10","resize":"none"})
        wid.append(inBDEL,'inBDEL')
        btMT = Button('Move To')
        btMT.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Move To')","class":"Button","editor_tag_type":"widget","editor_varname":"btMT"})
        btMT.style.update({"top":"847.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"17"})
        wid.append(btMT,'btMT')
        inMDIS = TextInput(True,'20')
        inMDIS.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'20')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inMDIS","placeholder":"20"})
        inMDIS.style.update({"top":"849.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"14","resize":"none"})
        wid.append(inMDIS,'inMDIS')
        inMDIR = TextInput(True,'0')
        inMDIR.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'0')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inMDIR","placeholder":"0"})
        inMDIR.style.update({"top":"850.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"12","resize":"none"})
        wid.append(inMDIR,'inMDIR')
        btRST = CLASSbtRST('Reset Software!')
        btRST.attributes.update({"editor_newclass":"True","editor_baseclass":"Button","editor_constructor":"('Reset Software!')","class":"Button","editor_tag_type":"widget","editor_varname":"btRST"})
        btRST.style.update({"top":"790.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"2"})
        wid.append(btRST,'btRST')
        LEDslider = Slider('50',0,100,5)
        LEDslider.attributes.update({"editor_newclass":"False","min":"0","max":"100","editor_baseclass":"Slider","editor_constructor":"('50',0,100,5)","editor_tag_type":"widget","value":"50","class":"range","autocomplete":"off","step":"5","editor_varname":"LEDslider","type":"range"})
        LEDslider.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"22"})
        wid.append(LEDslider,'LEDslider')
        btM = Button('Move')
        btM.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Move')","class":"Button","editor_tag_type":"widget","editor_varname":"btM"})
        btM.style.update({"top":"853.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"15"})
        wid.append(btM,'btM')
        btRS = Button('Reset Device')
        btRS.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Reset Device')","class":"Button","editor_tag_type":"widget","editor_varname":"btRS"})
        btRS.style.update({"top":"698.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"3"})
        wid.append(btRS,'btRS')
        inLDEL = TextInput(True,'0.001')
        inLDEL.attributes.update({"rows":"1","editor_baseclass":"TextInput","editor_constructor":"(True,'0.001')","class":"TextInput","autocomplete":"off","editor_tag_type":"widget","editor_newclass":"False","editor_varname":"inLDEL","placeholder":"0.001"})
        inLDEL.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"24","resize":"none"})
        wid.append(inLDEL,'inLDEL')
        btLP2 = CLASSbtLP2('Set to low power state 2')
        btLP2.attributes.update({"editor_newclass":"True","editor_baseclass":"Button","editor_constructor":"('Set to low power state 2')","class":"Button","editor_tag_type":"widget","editor_varname":"btLP2"})
        btLP2.style.update({"top":"607.765625px","height":"40px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"6"})
        wid.append(btLP2,'btLP2')
        btLP1 = Button('Set to low power state 1')
        btLP1.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Set to low power state 1')","class":"Button","editor_tag_type":"widget","editor_varname":"btLP1"})
        btLP1.style.update({"top":"605.765625px","height":"40px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"5"})
        wid.append(btLP1,'btLP1')
        btLFADE = Button('LED fade')
        btLFADE.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('LED fade')","class":"Button","editor_tag_type":"widget","editor_varname":"btLFADE"})
        btLFADE.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"25"})
        wid.append(btLFADE,'btLFADE')
        btFL = Button('Find travel limits')
        btFL.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Find travel limits')","class":"Button","editor_tag_type":"widget","editor_varname":"btFL"})
        btFL.style.update({"top":"588.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"8"})
        wid.append(btFL,'btFL')
        btMN = Button('Move to notch')
        btMN.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Move to notch')","class":"Button","editor_tag_type":"widget","editor_varname":"btMN"})
        btMN.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"20"})
        wid.append(btMN,'btMN')
        lbl6 = Label('LED Delay:')
        lbl6.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('LED Delay:')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl6"})
        lbl6.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"23"})
        wid.append(lbl6,'lbl6')
        lbl7 = Label('LED Power:')
        lbl7.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('LED Power:')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl7"})
        lbl7.style.update({"top":"20px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"21"})
        wid.append(lbl7,'lbl7')
        lbl4 = Label('Move to destination (Step)')
        lbl4.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Move to destination (Step)')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl4"})
        lbl4.style.update({"top":"855.765625px","height":"30px","width":"180px","position":"static","overflow":"auto","margin":"0px","order":"16"})
        wid.append(lbl4,'lbl4')
        lbl5 = Label('Move to notch (0 - 10)')
        lbl5.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Move to notch (0 - 10)')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl5"})
        lbl5.style.update({"top":"855.765625px","height":"30px","width":"150px","position":"static","overflow":"auto","margin":"0px","order":"18"})
        wid.append(lbl5,'lbl5')
        lbl2 = Label('Move direction (0 = Backwards, 1 = Forwards)')
        lbl2.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Move direction (0 = Backwards, 1 = Forwards)')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl2"})
        lbl2.style.update({"top":"592.765625px","height":"60px","width":"200px","position":"static","overflow":"auto","margin":"0px","order":"11"})
        wid.append(lbl2,'lbl2')
        lbl3 = Label('Move distance')
        lbl3.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Move distance')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl3"})
        lbl3.style.update({"top":"858.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"13"})
        wid.append(lbl3,'lbl3')
        lbl1 = Label('Delay settings:')
        lbl1.attributes.update({"editor_newclass":"False","editor_baseclass":"Label","editor_constructor":"('Delay settings:')","class":"Label","editor_tag_type":"widget","editor_varname":"lbl1"})
        lbl1.style.update({"top":"601.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"9"})
        wid.append(lbl1,'lbl1')
        btSS = Button('Change step size')
        btSS.attributes.update({"editor_newclass":"False","editor_baseclass":"Button","editor_constructor":"('Change step size')","class":"Button","editor_tag_type":"widget","editor_varname":"btSS"})
        btSS.style.update({"top":"647.765625px","height":"40px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"4"})
        wid.append(btSS,'btSS')
        btST = CLASSbtST('Get status')
        btST.attributes.update({"editor_newclass":"True","editor_baseclass":"Button","editor_constructor":"('Get status')","class":"Button","editor_tag_type":"widget","editor_varname":"btST"})
        btST.style.update({"top":"636.765625px","height":"30px","width":"100px","position":"static","overflow":"auto","margin":"0px","order":"7"})
        wid.append(btST,'btST')
        wid.children['btLSET'].onclick.connect(self.onclick_btLSET)
        wid.children['btSETT'].onclick.connect(self.onclick_btSETT)
        wid.children['btMT'].onclick.connect(self.onclick_btMT)
        wid.children['btRST'].onclick.connect(self.onclick_btRST)
        wid.children['btM'].onclick.connect(self.onclick_btM)
        wid.children['btRS'].onclick.connect(self.onclick_btRS)
        wid.children['btLP2'].onclick.connect(self.onclick_btLP2)
        wid.children['btLP1'].onclick.connect(self.onclick_btLP1)
        wid.children['btLFADE'].onclick.connect(self.onclick_btLFADE)
        wid.children['btFL'].onclick.connect(self.onclick_btFL)
        wid.children['btMN'].onclick.connect(self.onclick_btMN)
        wid.children['btSS'].onclick.connect(self.onclick_btSS)
        wid.children['btST'].onclick.connect(self.onclick_btST)
        

        self.wid = wid
        return self.wid
    
    

    def onclick_btSETT(self, emitter):
        self.wid.children['lbl'].set_text(BM.setup_triggers())

    def onclick_btRST(self, emitter):
        self.wid.children['lbl'].set_text(BM.setup())
        
    def onclick_btRS(self, emitter):
        self.wid.children['lbl'].set_text(BM.reset())
    
    def onclick_btSS(self, emitter):
        self.wid.children['lbl'].set_text(BM.stepSize1())
    
    def onclick_btLP1(self, emitter):
        self.wid.children['lbl'].set_text(BM.lowPower1())
    
    def onclick_btLP2(self, emitter):
        self.wid.children['lbl'].set_text(BM.lowPower2())
    
    def onclick_btST(self, emitter):
        self.wid.children['lbl'].set_text(BM.status())
    
    def onclick_btFL(self, emitter):
        self.wid.children['lbl'].set_text(BM.findLims(BM.BlindDelay))
        
    def onclick_btM(self, emitter):
        direct = int(float(self.wid.children['inMDIR'].get_text()))
        dist = int(float(self.wid.children['inMDIS'].get_text()))
        delay = float(self.wid.children['inBDEL'].get_text())
        BM.move(direct, dist, delay)
    
    def onclick_btMT(self, emitter):
        dest = int(float(self.wid.children['inMDES'].get_text()))
        delay = float(self.wid.children['inBDEL'].get_text())
        BM.moveto(dest, delay)
    
    def onclick_btMN(self, emitter):
        dest = int(float(self.wid.children['inMDEN'].get_text()))
        delay = float(self.wid.children['inBDEL'].get_text())
        BM.movetoNorm(dest, delay)
        
    def onclick_btLFADE(self, emitter):
        dest = int(float(self.wid.children['LEDslider'].get_value()))
        dela = float(self.wid.children['inLDEL'].get_text())
        BM.LEDfade(dest, delay = dela)
		
    def onclick_btLSET(self, emitter):
        dest = int(float(self.wid.children['LEDslider'].get_value()))
        BM.LEDfade(dest, delay = 0)



#Configuration
configuration = {'config_multiple_instance': True, 'config_address': '0.0.0.0', 'config_start_browser': True, 'config_enable_file_cache': True, 'config_project_name': 'untitled', 'config_resourcepath': './res/', 'config_port': 8081}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
