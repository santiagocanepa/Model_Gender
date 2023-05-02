import re


def possible_name(s):
    resultado = re.split('[^a-zA-Z0-9]+', s)[0]
    if len(resultado) > 1:
        return resultado
    else:
        return s


if __name__ == '__main__':

    print(possible_name("chinaa_sv"))
