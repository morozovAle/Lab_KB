# -*- coding: utf-8 -*-
import string

alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def decrypt(text):
    for change in range(1, 32):
        result = ""
        for i in text:
            if alf.find(i) != -1:
                j = alf.find(i)
                j = (j - change + len(alf)) % len(alf)
                result = result + alf[j]
            else:
                result = result + i
        if (result.find("добр") != -1) or (result.find("здравствуйте") != -1):
            print("Сдвиг:", change)
            print("Текст:\n", result)
            return result
    return -1

print("1)")
decrypt("блюншж явфвн, бйёпнёж яиэбёйёнляёф! оплизкриоь о еэбэфвж, злабэ кэ яштлбв квжнлккэь овпщ блидкэ яшбэяэпщ кв плищзл зиэоо (зиэооёсёзэуёь) ё кв мнлопл фёоил (нванвооёь). кэ яштлбв крдкл ялеянэцэпщ x, y, width, height ё зиэоо люкэнрдвкклал кэ зэнпёкзв лючвзпэ (ёиё зллнбёкэпш плфвз злкпрнля ъплал лючвзпэ, э-иь овайвкпэуёь).")
print("2)")
decrypt("эзъйфг эюжх. зйьщжвбщлзйф дмйкзы ийюэезавев люёф ийзюдлзы из дмйкм ai, зжв ы щллщрю. цлз жюзъшбщлюехжфю люёф, ыф ёзаюлю ыфъйщлх ечъмч кызч.")
print("3)")
decrypt("зрмцфмн ёпдзмрмфтёмы, зиса зтефян. ря х ёдрм еихизтёдпм ут очфхч фтхд отедпац. утпстъисстн уфтжфдрря рси сднцм си чздптха, пмьа цтпаот офдцомн упдс очфхд: ")
print("4)")
decrypt(" зтефян зиса. ёт ёпткисмм сдьи отррифыихоти уфизпткисми ут утотумнстрч техпчкмёдсмв. д цдоки хумхто уфизтхцдёпгирящ сдрм чхпчж. ечзир фдзя здпасиньирч уптзтцётфстрч хтцфчзсмыихцёч!")
print("5)")
decrypt("сьоюьт баюь. обсйат сьоюи этютшцыбай каьа внчщ ын ятюптю. каь сщм ныыи п кщтшаюцшб ьэцяныцт ыьътышщнабюи ынсь хнамыбай.")
print("6)")
decrypt("упьлнэюняхюр, пшфюьфх! шрщк уъняю щлюлчзк эрьоррнщл. к кнчкйэз ъафвфлчзщжш ыьрпэюлнфюрчршцьяыщъх ыьъфунъпэюнрщщъчъофэюфгрэцъх цъшылщфф. улщфшлршэк ыъэюлнцлшфыъ йоя ьъээфф.")
print("7)")
decrypt("тэпяйш туьк. рэ юуярйд samsung ai юяэрэтчб тън ьо 10сэ ыоабуя щъоаа р ысв. ")
print("8)")
decrypt("ощлыёф мпвпы, очуэыуф мцкоучуыщмув! ъщоьхксуэп, хщнок ю шкь люопэ ьцпоюидпп ткшйэуп?")
print("9)")
decrypt("ощлыёф опшж. мкг ъщвэщмёф йдух кхэумуыщмкцу.")
print("10)")
decrypt("чвфдоэ чшбп, жхуъушаоэ юяьшбё ! х гдвчвяъшбьш булшцв е хуаь чьуявцу- бугдухятс булш гдшчявъшбьш гв гвчюяскшбьс ьбёшдбшёу чят хулшэ вдцубьыуйьь!")