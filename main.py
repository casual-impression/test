from sys import exit
from random import randint
print("Играйте без читов... Для полного погружения.")


class Scene(object):
    def enter(self):
        print("Not implemented here yet.")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-----------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Finished(Scene):
    def enter(self):
        print("Ты победил! БРАВО!")
        exit(0)


class Death(Scene):
    quips = [
        "Ты умер. Научись играть, нубас!",
        "Твоя мама гордилась бы тобой... будь она умнее.",
        "Такой л-у-у-у-зер.",
        "Моя собака играет лучше, чем ты."
    ]

    def enter(self):
        print("Ты проиграл.")
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(0)


class CentralCorridor(Scene):

    def enter(self):
        print("""
Готонцы с планеты Персил-25 захватили твой корабль и уничтожили
оставшуюся часть команды. Ты остался один. Твоя последняя миссия -
достать разрушающую нейтронную бомбу из Оружейной Мастерской,
поместить её в корабль, и взорвать её вместе с кораблем сразу,
как только ты попадешь в спасательную шлюпку.

Ты бежишь вниз по Центральному Корридору в Оружейную Мастерскую,
как неожиданно выпрыгивает Готонец: красная чешуйчатая кожа,
тёмные от грязи зубы, одетый в костюм злого клоуна, обтекающий
его ненавистное тело. Он перекрывает путь к двери в Оружейную
и уже готов достать из кармана оружие для выстрела.
        """)
        print('варианты: "выстрелить", "уклониться", "рассказать шутку"')
        action = input("Твои действия: ")

        if action == "выстрелить":
            print("""
Быстрым движением ты достаешь из штанины бластер и выстреливаешь в
Готонца. Его костюм клоуна изменяет свое положение и передвигается
вокруг тела носителя, отклоняя твое предложение убийства. Твой лазер
попадает по костюму, но совершенно не попадает по владельцу. Такой
поворот событий абсолютно точно портит костюм клоуна (его Готонцу
купила мама). Готонец приходит в ярость! Он стреляет в ответ залпом
выстрелов в твое лицо, пока ему не надоест и ты не умрешь. Затем он
тебя ест.
            """)
            return 'death'

        elif action == "уклониться":
            print("""
Словно боксер мирового класса ты уклоняешься, покачиваясь из стороны
в сторону проскальзываешь к оппоненту и делаешь замах правой [пока
выстрел от бластера Готонца пролетает мимо вашей головы]!
В середине твоего изящного маневра ты подскальзываешься на банановой
кожуре, оставленного кем-то после обеда: происходит удар головой о
металлическую стену и ты отрубаешься... Однако сон продлился недолго.
Готонец уже медленно пожирает твои мозги, с интересом наблюдая за тем,
как мило ты барахтаешься в безнадежных попытках сбежать. Ты уже мертв!
            """)
            return 'death'

        elif action == "рассказать шутку":
            print("""
К счастью, в академии Морских Котиков ты изучил, как ввести Готонца в
состояние полного недоумения.
Ты рассказываешь Готонцу одну из шуток, которую ты только что сочинил:
'Заходят как-то в бар Программист, Морской Котик и Готонец ...'
Готонец останавливается в попытке не рассмеяться, затем истерично
хохочет, замирая на месте и не в силах остановиться.
Пока он смеется, ты подбегаешь, достаешь пистолет и стреляешь из бластера
прямо в голову недруга, укладывая его в состояние покоя.
После этого ты с удовлетворением входишь в Оружейную Мастерскую.
            """)
            return 'laser_weapon_armory'

        else:
            print("""
НЕ ВЫЧИСЛЯЕМО!
            """)
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("""
Ты погружаешься в Оружейную Мастерскую, приседаешь и сканируешь комнату,
чтобы найти больше Готонцев, которые могут скрываться.
Здесь довольно тихо. Слишком тихо.
Ты встаешь с колен и бежишь в дальний конец комнаты. Здесь ты находишь
нейтронную бомбу в контейнере. Чтобы её достать, тебе нужно взломать шифр
[брутфорс как вариант]. Блокировка клавиатуры - дело серьезное. Нужен код,
чтобы вытащить бомбу! НО ПОМНИТЕ... Если ты ошибетесь в выборе кода 10 раз,
замок закроется, и ты не сможешь получить бомбу. Код состоит из 3 цифр.
        """)
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[число]> ")
        guesses = 0

        while guess != code and guesses < 9:
            if guess > code:
                print("[Многовато будет]")
            elif guess < code:
                print("[Маловато будет]")
            else:
                print("[В самый раз! Как ты сюда попал?]")

            guesses += 1
            guess = input("[число]> ")

        if guess == code:
            print("""
Контейнер открывается, и уплотнение разрывается, выпуская газ. Ой, ой.
Ты нагло хватаешь нейтронную бомбу и бежишь так быстро, как только
можешь. К мосту! Там ты сможешь разместить бомбу в нужном месте.
            """)
            return 'the_bridge'
        else:
            print("""
Замок гудит в последний раз, после чего ты слышишь тошнотворный
тающий звук, когда механизм сливается воедино. Ты подумал, и решил остаться
на месте [ГЕНИАЛЬНО]. Готонцы от нечего делать взрывают корабль, и ты уже труп.
            """)
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print("""
С шумом ворвавшись на мост с нейтронной бомбой под мышкой, ты пытаешься удивить
пятерых Готонцев, которые пытаются взять под контроль корабль [ЗАЧЕМ?].
На каждом из них надет уродливый костюм клоуна, один страшнее другого.
Пришельцы уже хотели начать стрелять, но вскоре увидели большое страшную штуку
в твоих руках, как почему-то передумали. Дуракам закон не писан...
        """)

        print('варианты: "бросить бомбу", "медленно положить бомбу"')
        action = input("> ")

        if action == "бросить бомбу":
            print("""
В панике ты бросаешь нейтронную бомбу в группу Готонцев, надеясь на легкий
 испуг и счастливый конец, делая при этом отчаянный прыжок к двери. В момент
героического броска, один из Готонцев стреляет тебе прямо в спину [ПОДЛО],
убивая тебя. В последние секунды жизни ты наблюдаешь за тем, как другой
Готонец отчаяннопытается понять внутренний мир нейтронной! бомбы. Ты умрешь,
зная, что они, вероятно, взорвутся, так и не познав всю красоту этого мира.
            """)
            return 'death'

        elif action == "медленно положить бомбу":
            print("""
Решив, что терять уже нечего, вольной походкой ты проходишь мимо Готонцев,
указывая бластером на бомбу, что находится в свободной от бластера руке.
Готонцы подняли руки и начали потеть.
Ты подходишь к двери, открываешь ее, а затем осторожно клдешь бомбу на пол,
направив туда свой бластер.
Затем, резким движением ног, ты прыгаешь через дверь, нажимаешь кнопку,
закрытия, после чего стреляешь по системе управления дверью, чтобы Готонцы
не смогли выбраться из этой бессмысленной и беспощадной ситуации.
Теперь, когда бомба установлена, ты бежишь к спасательной капсуле, чтобы
сойти с этой консервной банки.
            """)
            return 'escape_pod'

        else:
            print("""
НЕ ВЫЧИСЛЯЕМО!
            """)
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print("""
Ты несешься через корабль, отчаянно пытаясь добраться до спасательный капсулы
прежде, чем произойдет взрыв целого корабля. Похоже на корабле почти нет
Готонцев, что приводит к некоторым логическим нестыковкам. Но об этом некогда
думать. Главное - продолжать бежать.
Ты попадаешь в секцию со спасательными капсулами.
Осталось только выбрать одну из них для спасения. Некоторые из них могут быть
повреждены, но у тебя нет времени смотреть.
Есть 5 капсул на выбор. На какой из них ты полетишь?
        """)

        g_pod1 = randint(1, 5)
        g_pod2 = randint(1, 5)
        g_pod3 = randint(1, 5)
        g_pod4 = randint(1, 5)

        guess = input("[№ капсулы]> ")

        if int(guess) in (g_pod1, g_pod2, g_pod3, g_pod4):
            print("Ты прыгаешь в модуль %s и жмёшь кнопку запуска." % guess)
            print("""
Капсула без проблем выдвигается в космос, направляясь к
соседней планете неподалёку. В момент полёта, через окно ты смотришь
назад, наблюдая за тем, как ТВОЙ корабль взрывается. Вскоре после
взрывается и находящийся в орбитальном пространстве корабль Готонцев
[Как? Почему? Зачем?]. Вспышка яркого света отблеском мелькнула в
твоих глазах. Ты выжил!
            """)
            return 'finished'
        else:
            print("Ты прыгаешь в модуль %s и жмёшь кнопку запуска." % guess)
            print("""
Капсула оказалась неуправляемой. Она некоторое время летит в пустоту
пространства, после чегов взрывается [корпус капсулы оказался не прочным],
разрушая твоё тело в желе, похожее на варенье. Печальный конец.
            """)
            return 'death'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
