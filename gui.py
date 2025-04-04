import tkinter as tk

class EchiquierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Échiquier")
        
        # Couleurs pour les cases
        self.couleur_claire = "#F0D9B5"  # beige clair
        self.couleur_foncee = "#B58863"  # marron
        
        # Taille de chaque case
        self.taille_case = 60
        
        # Créer le canvas pour dessiner l'échiquier
        self.canvas = tk.Canvas(root, width=8*self.taille_case, height=8*self.taille_case)
        self.canvas.pack()
        
        # Dessiner l'échiquier
        self.dessiner_echiquier()
    
    def dessiner_echiquier(self):
        for ligne in range(8):
            for colonne in range(8):
                # Déterminer la couleur de la case
                if (ligne + colonne) % 2 == 0:
                    couleur = self.couleur_claire
                else:
                    couleur = self.couleur_foncee
                
                # Dessiner la case
                x1 = colonne * self.taille_case
                y1 = ligne * self.taille_case
                x2 = x1 + self.taille_case
                y2 = y1 + self.taille_case
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")
                
                # Ajouter les coordonnées (optionnel)
                if ligne == 7:
                    self.canvas.create_text(x1 + 10, y2 - 10, text=chr(97 + colonne), fill="black" if couleur == self.couleur_claire else "white")
                if colonne == 0:
                    self.canvas.create_text(x1 + 10, y1 + 10, text=str(8 - ligne), fill="black" if couleur == self.couleur_claire else "white")

# Créer la fenêtre principale
if __name__ == "__main__":
    root = tk.Tk()
    app = EchiquierGUI(root)
    root.mainloop()

