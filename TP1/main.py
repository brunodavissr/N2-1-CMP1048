from jogo import *


def main():
    jogo = Jogo()
    continuar = True

    jogo.exibir_menu_principal()

    while continuar:
        jogo.exibir_menu_naves()
        finalizou_partida = jogo.gameplay()
        if(finalizou_partida):
            jogo.final_de_jogo()
            jogo = Jogo()
        else:
            jogo = Jogo()
            jogo.exibir_menu_principal()


if __name__ == "__main__":
    main()
