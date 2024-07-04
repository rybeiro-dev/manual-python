def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repetir_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repetir_msg('teste', 3)
