######################################################
### Main-Program                                   ###
### Projekt: BIZCIR-BW-01-Slave                    ###
### Version: 0.99          26.05.2026              ###
######################################################
from machine import Pin, Timer      # type: ignore
from libs.module_init import Global_Module as MyModule
import time                         # type: ignore

TIME_LOOP   = 0.01      # 10ms
TIME_DELAY  = 50        # x TIME_LOOP for Blink 

#------------------------------------------------------------------------------
pix_array_01 = [ 1]            # H2SAT
pix_array_02 = [ 2]            # EnMAP
pix_array_03 = [ 3, 4, 7]      # SARah             11, 12, 15   
pix_array_04 = [ 4]            # SAR-Lupe
pix_array_05 = [ 5]            # SATCOMBw
pix_array_06 = [ 5, 6]         # TerraSAR-X        13, 14
pix_array_07 = [ 7]            # SPOCK wird nicht dargestellt       
pix_array_08 = [ 1, 2]         # Galileo           9 , 10       
#---
pix_array_09 = [ 9]
pix_array_10 = [10]
pix_array_11 = [11]
pix_array_12 = [12]
pix_array_13 = [13]
pix_array_14 = [14]
pix_array_15 = [15]
pix_array_16 = [16]
#------------------------------------------------------------------------------

obj_offset = -1          # Offset bei Zählung ab 1 = -1

def blink_func():
    MyWS2812.do_blink()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    input_val       = 0x00
    blink_couter    = 0
    
    xio = MyXIO.XIO("INPUT")
    
    MyWS2812.do_all_def()	# Alle Leds auf Default-Wert
       
    while (True):

        if blink_couter > TIME_DELAY:
            blink_couter = 0
            blink_func()

        #print(hex(xio.read_io()))
        io_state = xio.read_io() & 0x0f
        #print(hex(io_state))
        if io_state != input_val:
            input_val = io_state
            if io_state == 0:
                print("State 0")
                MyWS2812.do_all_def()	# Alle Leds auf Default-Wert
            if io_state == 1:
                for i in pix_array_01:
                    print("State 1")
                    #MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 2:
                for i in pix_array_02:
                    print("State 2")
                    #MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 3:
                for i in pix_array_03:
                    print("State 3")
                    MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 4:
                for i in pix_array_04:
                    print("State 4")
                    #MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 5:
                for i in pix_array_05:
                    print("State 5")
                    #MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 6:
                for i in pix_array_06:
                    print("State 6")
                    MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 7:
                for i in pix_array_07:
                    print("State 7")
                    #MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 8:
                for i in pix_array_08:
                    print("State 8")
                    MyWS2812.set_led_obj(i + obj_offset, "blink")
            if io_state == 9:
                pass
        
        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(TIME_LOOP)


    

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()
    
    if MyModule.inc_xio:
        print("XIO -> Load-Module")
        import libs.module_xio_2 as MyXIO
    else:
        print("XIO -> nicht vorhanden")
    
    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")


    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
