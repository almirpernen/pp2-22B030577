def solve(head, leg):
    chikens = (leg - (4 * head)) / -2
    rabits = head - chikens
    return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}"