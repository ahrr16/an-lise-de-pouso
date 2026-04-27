from collections import deque
# Definição dos módulos da Estação Espacial em formato de lista, contendo as seguintes informações:
# [tipo, prioridade de pouso, nível de combustível, massa total, criticidade da carga, horário estimado de chegada à órbita, status operacional]

modulo_habitacao = ["Módulo de Habitação", 1, 0.8, 1000, 1, "2026-07-01 12:00:00",1]
modulo_energia = ["Módulo de Energia", 0.9, 0.7, 1277, 1, "2026-07-01 12:10:00",0.9]
modulo_laboratorio = ["Módulo de Laboratório", 0.8, 0.6, 1500, 0.8, "2026-07-01 12:20:00",0.5]
modulo_logistica = ["Módulo de Logística", 0.7, 0.8, 1000, 0.7, "2026-07-01 12:40:00",0.8]
modulo_medico = ["Módulo Médico", 1, 0.75, 1200, 1, "2026-07-01 12:30:00",1]

# Busca por módulos com menor combustível
for modulo in [modulo_habitacao, modulo_energia, modulo_laboratorio, modulo_logistica, modulo_medico]:
    if modulo[2] < 0.7:  # Verifica se o nível de combustível é inferior a 70%
        print(f"{modulo[0]} tem baixo combustível e deve ser priorizado para reabastecimento.")
# busca por módulos com maior combustível
for modulo in [modulo_habitacao, modulo_energia, modulo_laboratorio, modulo_logistica, modulo_medico]:
    if modulo[2] >= 0.7:  # Verifica se o nível de combustível é igual ou superior a 70%
        print(f"{modulo[0]} tem combustível suficiente e pode ser considerado para outras operações.")

# Busca por módulos pelo tipo de carga
tipos_carga = float(input("Digite o tipo de carga que deseja buscar (1 para crítica, 0 para não crítica): "))
for modulo in [modulo_habitacao, modulo_energia, modulo_laboratorio, modulo_logistica, modulo_medico]:
    if modulo[4] == tipos_carga:  # Verifica se a criticidade da carga é alta
        print(f"{modulo[0]} ")

# Definição da ordem de pouso por horário estimado de chegada à órbita
prioridade = deque([])
for horario in [modulo_habitacao, modulo_energia, modulo_laboratorio, modulo_logistica, modulo_medico]:
    match horario[5]:  # Verifica o horário estimado de chegada à órbita
        case "2026-07-01 12:00:00":
            prioridade.append(horario[0])
        case "2026-07-01 12:10:00":
            prioridade.append(horario[0])
        case "2026-07-01 12:20:00":
            prioridade.append(horario[0])
        case "2026-07-01 12:30:00":
            prioridade.append(horario[0])
        case "2026-07-01 12:40:00":
            prioridade.append(horario[0])

print("Ordem de pouso por horário estimado de chegada à órbita:", prioridade)

# Definição das condições de pouso
clima = ['Limpo', 'Nublado', 'Chuvoso', 'Tempestade']
area_pouso = ['Livre', 'Obstruída']

# Módulos pousados
modulos_pousados = []
modulos_espera = []
for modulo in [modulo_habitacao, modulo_energia, modulo_laboratorio, modulo_logistica, modulo_medico]:
    if modulo[1] >= 0.8 and clima[0] ==('Limpo' or 'Nublado' or 'Chuvoso') and area_pouso[0] == 'Livre':
        modulos_pousados.append(modulo[0])
    else:
        modulos_espera.append(modulo[0])
print('Módulos pousados:', modulos_pousados)
print('Módulos em espera:', modulos_espera)