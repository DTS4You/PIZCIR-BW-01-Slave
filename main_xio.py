import asyncio
from libs.modul_xio_bus import ParallelBus
import libs.modul_hwdebug as mydebug

# Bus-Instanz erstellen
bus = ParallelBus(
    data_pins=[10, 11, 12, 13], pin_strobe_high=14, pin_strobe_low=15
)

hwdebug = mydebug.HWDEBUG()

global debug_led

debug_led = True  # Variable für die Debug-LED (True = LED an, False = LED aus)

def on_string_received(text):
    global debug_led
    print(f"[RX Event] Empfangener Text: '{text}' (Länge: {len(text)})")
    hwdebug.write_output(debug_led)  # LED einschalten
    debug_led = not debug_led  # Toggle der LED-Variable

async def main():
    print("RP2040 Bus aktiv (Modul geladen). Empfange Daten...")

    # Empfänger-Task aus der Modul-Klasse starten
    asyncio.create_task(bus.listen_loop(on_string_received))

    while True:
        await asyncio.sleep(0.3)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nProgramm gestoppt.")

