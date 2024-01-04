class Tanda:
    """
        Tanda model.
    """

    def __init__(self, name: str, participants: list[str], amount: float, period: int):
        self.name = name
        self.participants = participants
        self.amount = amount
        self.period = period
        self.total_amount = amount * period
        self.current_amount = 0
        self.current_round = 0
        self.current_round_participants = []
        self.current_round_payments = {}
        self.current_round_payments_count = 0
        self.current_round_payments_total = 0
        self.current_round_payments_average = 0
        self.current_round_payments_average_rounded = 0
        self.current_round_payments_average_rounded_str = ""
