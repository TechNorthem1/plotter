import serial

def generate_hpgl_commands():
    commands = []
    commands.append("IN;")  # Inicializar el plotter
    commands.append("SP1;")  # Seleccionar la pluma 1
    commands.append("PU0,0;")  # Levantar la pluma (Pen Up) y mover a la posición inicial (0,0)
    commands.append("PD1000,0;")  # Bajar la pluma (Pen Down) y mover a (1000,0)
    commands.append("PD1000,1000;")  # Mover a (1000,1000)
    commands.append("PD0,1000;")  # Mover a (0,1000)
    commands.append("PD0,0;")  # Mover a (0,0)
    commands.append("PU;")  # Levantar la pluma
    return "\n".join(commands)

# Función para enviar comandos al plotter
def send_to_plotter(port, commands):
    with serial.Serial(port, 9600, timeout=1) as ser:
        ser.write(commands.encode('ascii'))

if __name__ == "__main__":
    hpgl_commands = generate_hpgl_commands()
    port = "/dev/ttyUSB0"  # Asegúrate de cambiar esto por el puerto correcto
    send_to_plotter(port, hpgl_commands)