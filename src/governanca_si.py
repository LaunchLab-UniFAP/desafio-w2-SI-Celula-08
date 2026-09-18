# LaunchLab UniFAP - Desenvolvimento Exclusivo SI
METADADOS_COMPLIANCE = {
    "limite_frota_m3": 50.0,
    "teto_ociosidade_percentual": 0.30,
    "piso_ociosidade_percentual": 0.30,
    "indicadores_ambientais": ["Reducao CO2", "Economia Combustivel"]
}

def calcular_eficiencia_financeira(volume_final):
    if not isinstance(volume_final, (int, float)) or isinstance(volume_final, bool):
        return "Erro: Volume Invalido"

    capacidade = METADADOS_COMPLIANCE["limite_frota_m3"]

    if volume_final < 0 or volume_final > capacidade:
        return "Erro: Volume Invalido"

    percentual_uso = (volume_final / capacidade) * 100
    percentual_ociosidade = 100 - percentual_uso
    volume_minimo = capacidade * METADADOS_COMPLIANCE["teto_ociosidade_percentual"]

    if volume_final < volume_minimo:
        return "Alerta: Alto Custo de Ociosidade Detectado"

    return "Eficiencia Economica Aceitavel"

if __name__ == "__main__":
    print(calcular_eficiencia_financeira(12.5)) 
