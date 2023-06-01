team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]

cards = input()

split_cards = cards.split(" ")
# for card in split_cards:
#     print(card)
# print(split_cards)

terminated = False

if split_cards:
    used_cards = []
    for card in split_cards:
        if card not in used_cards:
            used_cards.append(card)
            current_card = card.split("-")
            if current_card[0] == "A":
                index_adjustment_a = 11 - len(team_a)
                team_a.pop(int(current_card[1]) - 1 - index_adjustment_a)
            elif current_card[0] == "B":
                index_adjustment_b = 11 - len(team_b)
                team_b.pop(int(current_card[1]) - 1 - index_adjustment_b)
        else:
            continue
        if len(team_a) < 7 or len(team_b) < 7:
            print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
            print("Game was terminated")
            terminated = True
            break
        else:
            continue
    if not terminated:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")


# ChatGPT solution
# cards = input().split()
# team_A_players = set(range(1, 12))
# team_B_players = set(range(1, 12))
#
# for card in cards:
#     team, player = card.split('-')
#     player = int(player)
#
#     if team == 'A' and player in team_A_players:
#         team_A_players.remove(player)
#     elif team == 'B' and player in team_B_players:
#         team_B_players.remove(player)
#
#     if len(team_A_players) < 7 or len(team_B_players) < 7:
#         print("Game was terminated")
#         break
#
# print(f"Team A - {len(team_A_players)}; Team B - {len(team_B_players)}")