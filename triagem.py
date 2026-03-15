def classificar(temperatura, dor):

    if temperatura >= 40 or dor >= 9:
        return "SUPERURGENTE"

    elif temperatura >= 39 or dor >= 7:
        return "URGENTE"

    elif dor >= 4:
        return "MODERADO"

    else:
        return "TRANQUILO"