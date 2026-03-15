function classificarPaciente(dor, temperatura, respiracao) {

    if (resppiracao === "grave") {
        return "SUPERURGENTE - atendimento imediato";
    }

    if (temperatura > 39 || dor >= 8) {
        return "URGENTE - atendimento em até 10 minutos";
    }

    if (dor >= 4) {
        return "MODERADO - atendimento ematé 2 horas";
    }

    return "TRANQUILO - atendimento em até 4 horas";
}