class Post:
    def __init__(self, titulo, contenido, autor="Usuario"):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.likes = 0

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def dar_like(self):
        self.likes += 1

# --- Simulando una base de datos de recetas ---
feed_gastronomico = [
    Post("Ñoquis del Domingo", "Receta de la abuela con mucha salsa roja."),
    Post("Mi Fideo con Huevo", "Rápido, fácil y con mucho queso rallado."),
    Post("Pizza Casera", "Masa de 24hs de leudado.")
]

# Probar la lógica:
for p in feed_gastronomico:
    print(f"Publicando: {p}")

    