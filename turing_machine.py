class TuringMachine:
    def __init__(self, tape_string):
        # We append a blank space '_' at the end of the tape
        self.tape = list(tape_string) + ['_']
        self.head_position = 0
        self.state = 'q0'
        self.accept_state = 'q_accept'
        self.reject_state = 'q_reject'
        
        # Transition Table (Durum Geçiş Tablosu)
        # Matematiksel tanım: delta(durum, okunan_sembol) -> yeni_durum
        self.transitions = {}
        digits = "0123456789"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # N (Rakam) bekleyen durum geçişleri
        for d in digits:
            self.transitions[('q0', d)] = 'q1'
            self.transitions[('q1', d)] = 'q2'
            self.transitions[('q4', d)] = 'q5'
            self.transitions[('q5', d)] = 'q6'
            self.transitions[('q6', d)] = 'q7'
            
        # L (Harf) bekleyen durum geçişleri
        for l in letters:
            self.transitions[('q2', l)] = 'q3'
            self.transitions[('q3', l)] = 'q4'
            
        # Bitiş (Boşluk) kontrol geçişi
        self.transitions[('q7', '_')] = self.accept_state

    def step(self):
        char = self.tape[self.head_position]
        old_state = self.state
        
        # Geçiş fonksiyonunu işlet (Tablodan bak)
        # Eğer okunan sembol bulunduğumuz duruma ait tablodaki kurallarda yoksa RED durumuna at.
        self.state = self.transitions.get((self.state, char), self.reject_state)

        move = "R" if self.state != self.reject_state and self.state != self.accept_state else "-"
        
        print(f"Durum: {old_state}, Okunan: '{char}', Yeni Durum: {self.state}, Kafa Hareketi: {move}, Bant: {''.join(self.tape)}")
        
        if move == "R":
            self.head_position += 1

    def run(self):
        print(f"--- Simülasyon Başlıyor ---")
        print(f"Başlangıç Bandı: {''.join(self.tape)}")
        while self.state not in [self.accept_state, self.reject_state]:
            if self.head_position >= len(self.tape):
                # Should not happen as we pad with '_', but just in case
                self.state = self.reject_state
                break
            self.step()
        
        print("-" * 30)
        if self.state == self.accept_state:
            print("Sonuç: KABUL")
        else:
            print("Sonuç: RED")

if __name__ == "__main__":
    import sys
    print("Turing Makinesi Plaka Tanıyıcı (Format: NNLLNNN)")
    print("-----------------------------------------------")
    
    # If arguments are passed, don't use input loop, just run tests
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        tests = [
            ("55AB123", True),
            ("34TR456", True),
            ("06AA789", True),
            ("35ZX321", True),
            ("01ZZ000", True),
            ("5AB123", False),
            ("555AB12", False),
            ("34A1234", False),
            ("AB34123", False),
            ("34AB12X", False),
            ("55ab123", False)
        ]
        
        for plaka, expected in tests:
            print(f"\n[TEST GİRDİSİ]: {plaka}")
            tm = TuringMachine(plaka)
            tm.run()
        sys.exit(0)

    print("Çıkmak için 'q' veya 'quit' yazabilirsiniz.\n")
    while True:
        try:
            plaka = input("Lütfen kontrol edilecek plakayı girin: ")
            if plaka.lower() in ['q', 'quit']:
                break
            
            tm = TuringMachine(plaka)
            tm.run()
            print("\n")
        except EOFError:
            break