import traci
from sumolib import checkBinary

def prueba_control():
    # Iniciamos con interfaz para ver el cambio
    traci.start([checkBinary('sumo-gui'), "-c", "nexus.sumocfg"])
    
    print("🚦 Probando control del Nexus...")
    
    # 1. Vamos a poner el N3 (el más grande) en VERDE TOTAL
    # Como nos dijiste que tiene 21 letras, mandamos 21 'G'
    fase_verde_n3 = "G" * 21
    traci.trafficlight.setRedYellowGreenState("N3", fase_verde_n3)
    
    # 2. Vamos a poner el N6 (el más chico) en ROJO TOTAL
    fase_roja_n6 = "r" * 4
    traci.trafficlight.setRedYellowGreenState("N6", fase_roja_n6)

    # Corremos 50 pasos para observar
    for step in range(50):
        traci.simulationStep()
        # Aquí la IA leería cuántos coches hay en 'E'
        coches = traci.edge.getLastStepHaltingNumber('E')
        if step % 10 == 0:
            print(f"Paso {step}: Hay {coches} coches esperando en la calle 'E'")

    traci.close()
    print("✅ Prueba de control terminada.")

if __name__ == "__main__":
    prueba_control()


# taskkill /f /im sumo-gui.exe /t