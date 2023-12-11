import random
from colorama import Fore, Back, Style
def generate_player():
    player=dict()
    player[0]=150
    player[1]=10
    return player
def print_stats(player):
    print(Fore.GREEN+f"Здоровье: {player[0]} \nСила атаки: {player[1]}\n___________"+Fore.WHITE)
def generate_enemy():
    enemies_dict=dict(goblin=["Гоблин", 15, 5],                      
    ork=["Орк", 25, 7],
    bandit=["Бандит", 30, 8],                      
    wamp=["Вампир", 45, 10],
    dragon=["Дракон", 55, 12])
    enemy_chance = random.randint(0, 4)
    if enemy_chance==0:
        enemy_name=enemies_dict["goblin"]    
    if enemy_chance==1:
        enemy_name=enemies_dict["ork"]    
    if enemy_chance==2:
        enemy_name=enemies_dict["bandit"]    
    if enemy_chance==3:
        enemy_name=enemies_dict["wamp"]    
    if enemy_chance==4:
        enemy_name=enemies_dict["dragon"]
    return [enemy_name, enemies_dict]
def fight(player, enemy_name):
    if player[0]>=0 or enemy_name[1]>=0:
        player[0]-=enemy_name[2]
        enemy_name[1]-=player[1]
        if player[0]>=0:     
            print(f'Вы одолели {enemy_name[0]}а')
            return True
        else:
            print(Fore.RED +"Вы погибли")
            return False
    else:
        print(Fore.RED + "теперь вы призрак... ")
        return False
def explore(player, enemy_name):
    chance=random.random()*1
    if chance<0.7:
        generate_enemy()
        print(f' вы встретили {enemy_name[0]}')
        while True:
            try:
                e=int(input('сразиться с врагом "1", либо сбежать от боя "2".'))
                break
            except:
                print(Fore.RED + "Ошибка ввода" + Fore.WHITE)
        if e == 1:
            fight(player, enemy_name)
        else:
            a=random.randint(1, 2)
            if a==2:
                print("вы сбежали...")   
            else:
                print("сбежать не удалось, придётся сражаться...")
                fight(player, enemy_name)
            if chance>0.7:
                print("Вы нашли безхозный дом, отдохнуть?")
                print('да "1", нет "2"')
                d=int(input())
                if d==1:
                    player[0]=150
            print("Силы востановлены,  можете продолжать путь!")   
def play_game():
    player=generate_player()
    while True and player[0]>=0:
        enemy_name=generate_enemy()[0]
        print_stats(player)
        i=int(input('Исследовать игровую среду "1" или выйти из игры "2".'))
        if i==1:
            explore(player, enemy_name)
        elif i==2:
            print("До скорой встречи!")
            break
        else:
            print("Нет такого варианта ответа!")
            continue
    print(Fore.BLUE + "Конец Игры")
play_game()