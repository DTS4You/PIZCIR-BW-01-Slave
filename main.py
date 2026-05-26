######################################################
### Main-Program                                   ###
### Projekt: BIZCIR-BW-01-Slave                    ###
### Version: 0.99          26.05.2026              ###
######################################################
from machine import Pin, Timer      # type: ignore
from libs.module_init import Global_Module as MyModule
import time                         # type: ignore

TIME_LOOP   = 0.1
TIME_DELAY  = 10 

#------------------------------------------------------------------------------
pix_array_01 = [ 1]
pix_array_02 = [ 2]
pix_array_03 = [ 3]
pix_array_06 = [ 4]
pix_array_04 = [ 5]
pix_array_05 = [ 6]
pix_array_07 = [ 7]
pix_array_08 = [ 8]
pix_array_09 = [ 9]
pix_array_10 = [10]
pix_array_11 = [11]
pix_array_12 = [12]
pix_array_13 = [13]
pix_array_14 = [14]
pix_array_15 = [15]
pix_array_16 = [16]
#------------------------------------------------------------------------------

obj_offset = 0          # Offset bei Zählung ab 1 = -1

def blink_func():
    MyWS2812.do_blink()


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")

    xio = MyXIO.XIO("INPUT")
    
    MyWS2812.do_all_def()	# Alle Leds auf Default-Wert
       
    while (True):
        print(hex(xio.read_io()))
        io_state = xio.read_io()
        if io_state == 0:
            pass
        if io_state == 1:
            for i in pix_array_01:
                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
        if io_state == 2:
            pass
        
    time.sleep(TIME_LOOP)


    

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
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
        #print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")


    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
