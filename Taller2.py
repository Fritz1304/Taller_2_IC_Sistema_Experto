import tkinter as tk
from tkinter import ttk, messagebox
from pyknow import KnowledgeEngine, Fact, Rule

class CityActivity(Fact):
    pass

class CityActivityExpert(KnowledgeEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recommended_activity = None

    # Reglas para Bogotá
    @Rule(CityActivity(city='bogotá', climate='soleado', budget='bajo'))
    def bogota_sunny_low_budget(self):
        self.recommended_activity = 'Visitar el Parque Simón Bolívar'

    @Rule(CityActivity(city='bogotá', climate='soleado', budget='medio'))
    def bogota_sunny_medium_budget(self):
        self.recommended_activity = 'Tour histórico por La Candelaria'

    @Rule(CityActivity(city='bogotá', climate='soleado', budget='alto'))
    def bogota_sunny_high_budget(self):
        self.recommended_activity = 'Degustar la gastronomía en Usaquén'

    @Rule(CityActivity(city='bogotá', climate='lluvioso', budget='bajo'))
    def bogota_rainy_low_budget(self):
        self.recommended_activity = 'Explorar museos como el Museo del Oro'

    @Rule(CityActivity(city='bogotá', climate='lluvioso', budget='medio'))
    def bogota_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a eventos culturales en teatros'

    @Rule(CityActivity(city='bogotá', climate='lluvioso', budget='alto'))
    def bogota_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en spas y centros de bienestar'

    @Rule(CityActivity(city='bogotá', climate='nublado', budget='bajo'))
    def bogota_cloudy_low_budget(self):
        self.recommended_activity = 'Explorar el centro histórico y mercados locales'

    @Rule(CityActivity(city='bogotá', climate='nublado', budget='medio'))
    def bogota_cloudy_medium_budget(self):
        self.recommended_activity = 'Visitar galerías de arte y eventos culturales'

    @Rule(CityActivity(city='bogotá', climate='nublado', budget='alto'))
    def bogota_cloudy_high_budget(self):
        self.recommended_activity = 'Disfrutar de la gastronomía local en restaurantes'

    @Rule(CityActivity(city='bogotá', climate='templado', budget='bajo'))
    def bogota_mild_low_budget(self):
        self.recommended_activity = 'Recorrido por parques y zonas verdes.'   

    @Rule(CityActivity(city='bogotá', climate='templado', budget='medio'))
    def bogota_mild_medium_budget(self):
        self.recommended_activity = 'Tour histórico por la ciudad'   

    @Rule(CityActivity(city='bogotá', climate='templado', budget='alto'))
    def bogota_mild_high_budget(self):
        self.recommended_activity = 'Degustar la gastronomía local en mercados'

    # Reglas para Cali
    @Rule(CityActivity(city='cali', climate='soleado', budget='bajo'))
    def cali_sunny_low_budget(self):
        self.recommended_activity = 'Bailar salsa en La Topa Tolondra.'

    @Rule(CityActivity(city='cali', climate='soleado', budget='medio'))
    def cali_sunny_medium_budget(self):
        self.recommended_activity = 'Visitar el Gato de Tejada.'

    @Rule(CityActivity(city='cali', climate='soleado', budget='alto'))
    def cali_sunny_high_budget(self):
        self.recommended_activity = 'Cena en Platillos Voladores.'

    @Rule(CityActivity(city='cali', climate='lluvioso', budget='bajo'))
    def cali_rainy_low_budget(self):
        self.recommended_activity = 'Explorar el Museo La Tertulia.'

    @Rule(CityActivity(city='cali', climate='lluvioso', budget='medio'))
    def cali_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a un concierto en el Teatro Jorge Isaacs.'

    @Rule(CityActivity(city='cali', climate='lluvioso', budget='alto'))
    def cali_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el Spa Makawé'

    @Rule(CityActivity(city='cali', climate='nublado', budget='bajo'))
    def cali_cloudy_low_budget(self):
        self.recommended_activity = 'Visitar el Centro Cultural de Cali.'

    @Rule(CityActivity(city='cali', climate='nublado', budget='medio'))
    def cali_cloudy_medium_budget(self):
        self.recommended_activity = 'Recorrido por el Parque de los Poetas.'

    @Rule(CityActivity(city='cali', climate='nublado', budget='alto'))
    def cali_cloudy_high_budget(self):
        self.recommended_activity = 'Cena gourmet en Platillos Voladores.'

    @Rule(CityActivity(city='cali', climate='templado', budget='bajo'))
    def cali_mild_low_budget(self):
        self.recommended_activity = 'Paseo por el Zoológico de Cali.'

    @Rule(CityActivity(city='cali', climate='templado', budget='medio'))
    def cali_mild_medium_budget(self):
        self.recommended_activity = 'Tour de la Plaza de Cayzedo.'

    @Rule(CityActivity(city='cali', climate='templado', budget='alto'))
    def cali_mild_high_budget(self):
        self.recommended_activity = 'Cena en Platillos Voladores.'

    # Reglas para Medellín
    @Rule(CityActivity(city='medellín', climate='soleado', budget='bajo'))
    def medellin_sunny_low_budget(self):
        self.recommended_activity = 'Visitar el Jardín Botánico.'

    @Rule(CityActivity(city='medellín', climate='soleado', budget='medio'))
    def medellin_sunny_medium_budget(self):
        self.recommended_activity = 'Recorrido por el Pueblito Paisa.'

    @Rule(CityActivity(city='medellín', climate='soleado', budget='alto'))
    def medellin_sunny_high_budget(self):
        self.recommended_activity = 'Cena en Carmen.'

    @Rule(CityActivity(city='medellín', climate='lluvioso', budget='bajo'))
    def medellin_rainy_low_budget(self):
        self.recommended_activity = 'Explorar el Museo de Antioquia.'

    @Rule(CityActivity(city='medellín', climate='lluvioso', budget='medio'))
    def medellin_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a un espectáculo en el Teatro Metropolitano.'

    @Rule(CityActivity(city='medellín', climate='lluvioso', budget='alto'))
    def medellin_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el Spa del Hotel Dann Carlton.'

    @Rule(CityActivity(city='medellín', climate='templado', budget='bajo'))
    def medellin_mild_low_budget(self):
        self.recommended_activity = 'Paseo en el Parque Explora.'

    @Rule(CityActivity(city='medellín', climate='templado', budget='medio'))
    def medellin_mild_medium_budget(self):
        self.recommended_activity = 'Tour gastronómico por el Mercado del Río.'

    @Rule(CityActivity(city='medellín', climate='templado', budget='alto'))
    def medellin_mild_high_budget(self):
        self.recommended_activity = 'Cena en El Cielo.'

    @Rule(CityActivity(city='medellín', climate='nublado', budget='bajo'))
    def medellin_cloudy_low_budget(self):
        self.recommended_activity = 'Visitar el Museo El Castillo.'

    @Rule(CityActivity(city='medellín', climate='nublado', budget='medio'))
    def medellin_cloudy_medium_budget(self):
        self.recommended_activity = 'Recorrido por el Barrio Provenza.'

    @Rule(CityActivity(city='medellín', climate='nublado', budget='alto'))
    def medellin_cloudy_high_budget(self):
        self.recommended_activity = 'Cena en Oci.Mde.'

    # Reglas para Cartagena
    @Rule(CityActivity(city='cartagena', climate='soleado', budget='bajo'))
    def cartagena_sunny_low_budget(self):
        self.recommended_activity = 'Explorar las murallas y el Centro Histórico.'

    @Rule(CityActivity(city='cartagena', climate='soleado', budget='medio'))
    def cartagena_sunny_medium_budget(self):
        self.recommended_activity = 'Paseo en barco por las Islas del Rosario.'

    @Rule(CityActivity(city='cartagena', climate='soleado', budget='alto'))
    def cartagena_sunny_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Vera.'

    @Rule(CityActivity(city='cartagena', climate='lluvioso', budget='bajo'))
    def cartagena_rainy_low_budget(self):
        self.recommended_activity = 'Visitar el Museo Histórico de Cartagena.'

    @Rule(CityActivity(city='cartagena', climate='lluvioso', budget='medio'))
    def cartagena_rainy_medium_budget(self):
        self.recommended_activity = 'Recorrido por el Convento de la Popa.'

    @Rule(CityActivity(city='cartagena', climate='lluvioso', budget='alto'))
    def cartagena_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el spa del Hotel Santa Clara.'

    @Rule(CityActivity(city='cartagena', climate='templado', budget='bajo'))
    def cartagena_mild_low_budget(self):
        self.recommended_activity = 'Recorrer la Ciudad Amurallada en coche de caballos.'
    
    @Rule(CityActivity(city='cartagena', climate='templado', budget='medio'))
    def cartagena_mild_medium_budget(self):
        self.recommended_activity = 'Tour gastronómico por la Calle del Santísimo.'

    @Rule(CityActivity(city='cartagena', climate='templado', budget='alto'))
    def cartagena_mild_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Alma.'

    @Rule(CityActivity(city='cartagena', climate='nublado', budget='bajo'))
    def cartagena_cloudy_low_budget(self):
        self.recommended_activity = 'Visitar la Plaza de la Aduana.'

    @Rule(CityActivity(city='cartagena', climate='nublado', budget='medio'))
    def cartagena_cloudy_medium_budget(self):
        self.recommended_activity = 'Recorrer el Museo Naval del Caribe.'

    @Rule(CityActivity(city='cartagena', climate='nublado', budget='alto'))
    def cartagena_cloudy_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Alma.'

    # Nuevas ciudades

    @Rule(CityActivity(city='barranquilla', climate='soleado', budget='bajo'))
    def barranquilla_sunny_low_budget(self):
        self.recommended_activity = 'Explorar el barrio El Prado.'

    @Rule(CityActivity(city='barranquilla', climate='soleado', budget='medio'))
    def barranquilla_sunny_medium_budget(self):
        self.recommended_activity = 'Visitar el Museo del Caribe.'

    @Rule(CityActivity(city='barranquilla', climate='soleado', budget='alto'))
    def barranquilla_sunny_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante El Sombrero Vueltiao.'

    @Rule(CityActivity(city='barranquilla', climate='lluvioso', budget='bajo'))
    def barranquilla_rainy_low_budget(self):
        self.recommended_activity = 'Conocer el Museo Romántico.'

    @Rule(CityActivity(city='barranquilla', climate='lluvioso', budget='medio'))
    def barranquilla_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a un espectáculo en el Teatro Amira de la Rosa.'

    @Rule(CityActivity(city='barranquilla', climate='lluvioso', budget='alto'))
    def barranquilla_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el spa del Hotel Dann Carlton.'

    @Rule(CityActivity(city='barranquilla', climate='nublado', budget='bajo'))
    def barranquilla_cloudy_low_budget(self):
        self.recommended_activity = 'Visitar el Centro Histórico de Barranquilla.'

    @Rule(CityActivity(city='barranquilla', climate='nublado', budget='medio'))
    def barranquilla_cloudy_medium_budget(self):
        self.recommended_activity = 'Recorrer la Plaza de la Paz.'

    @Rule(CityActivity(city='barranquilla', climate='nublado', budget='alto'))
    def barranquilla_cloudy_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante El Sombrero Vueltiao.'

    @Rule(CityActivity(city='barranquilla', climate='templado', budget='bajo'))
    def barranquilla_mild_low_budget(self):
        self.recommended_activity = 'Paseo en bote por el río Magdalena.'

    @Rule(CityActivity(city='barranquilla', climate='templado', budget='medio'))
    def barranquilla_mild_medium_budget(self):
        self.recommended_activity = 'Tour gastronómico por el centro histórico.'
    
    @Rule(CityActivity(city='barranquilla', climate='templado', budget='alto'))
    def barranquilla_mild_high_budget(self):
        self.recommended_activity = 'Disfrutar de la gastronomía local en restaurantes'

    @Rule(CityActivity(city='pereira', climate='soleado', budget='bajo'))
    def pereira_sunny_low_budget(self):
        self.recommended_activity = 'Paseo por el Parque El Lago.'

    @Rule(CityActivity(city='pereira', climate='soleado', budget='medio'))
    def pereira_sunny_medium_budget(self):
        self.recommended_activity = 'Tour histórico por el centro de Pereira.'

    @Rule(CityActivity(city='pereira', climate='soleado', budget='alto'))
    def pereira_sunny_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Don Jediondo.'

    @Rule(CityActivity(city='pereira', climate='lluvioso', budget='bajo'))
    def pereira_rainy_low_budget(self):
        self.recommended_activity = 'Visitar el Museo de Arte de Pereira.'

    @Rule(CityActivity(city='pereira', climate='lluvioso', budget='medio'))
    def pereira_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a eventos culturales en el Teatro Santiago Londoño.'

    @Rule(CityActivity(city='pereira', climate='lluvioso', budget='alto'))
    def pereira_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el spa del Hotel Movich.'

    @Rule(CityActivity(city='pereira', climate='templado', budget='bajo'))
    def pereira_mild_low_budget(self):
        self.recommended_activity = 'Recorrido por el Jardín Botánico.'

    @Rule(CityActivity(city='pereira', climate='templado', budget='medio'))
    def pereira_mild_medium_budget(self):
        self.recommended_activity = 'Tour gastronómico por la Avenida Circunvalar.'

    @Rule(CityActivity(city='pereira', climate='templado', budget='alto'))
    def pereira_mild_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Barbas Bistró.'

    @Rule(CityActivity(city='pereira', climate='nublado', budget='bajo'))
    def pereira_cloudy_low_budget(self):
        self.recommended_activity = 'Explorar el Centro Cultural Lucy Tejada.'

    @Rule(CityActivity(city='pereira', climate='nublado', budget='medio'))
    def pereira_cloudy_medium_budget(self):
        self.recommended_activity = 'Visitar el Parque Olaya Herrera.'

    @Rule(CityActivity(city='pereira', climate='nublado', budget='alto'))
    def pereira_cloudy_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Barbas Bistró.'

    @Rule(CityActivity(city='manizales', climate='soleado', budget='bajo'))
    def manizales_sunny_low_budget(self):
        self.recommended_activity = 'Explorar el Recinto del Pensamiento.'
    
    @Rule(CityActivity(city='manizales', climate='soleado', budget='medio'))
    def manizales_sunny_medium_budget(self):
        self.recommended_activity = 'Tour gastronómico por la Avenida Santander.'

    @Rule(CityActivity(city='manizales', climate='soleado', budget='alto'))
    def manizales_sunny_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Termales El Otoño.'
    
    @Rule(CityActivity(city='manizales', climate='lluvioso', budget='bajo'))
    def manizales_rainy_low_budget(self):
        self.recommended_activity = 'Visitar el Museo de Arte de Caldas.'

    @Rule(CityActivity(city='manizales', climate='lluvioso', budget='medio'))
    def manizales_rainy_medium_budget(self):
        self.recommended_activity = 'Asistir a eventos culturales en el Teatro Los Fundadores.'

    @Rule(CityActivity(city='manizales', climate='lluvioso', budget='alto'))
    def manizales_rainy_high_budget(self):
        self.recommended_activity = 'Relajarse en el spa del Hotel Estelar Recinto del Pensamiento.'

    @Rule(CityActivity(city='manizales', climate='templado', budget='bajo'))
    def manizales_mild_low_budget(self):
        self.recommended_activity = 'Recorrido por el Jardín Botánico.'

    @Rule(CityActivity(city='manizales', climate='templado', budget='medio'))
    def manizales_mild_medium_budget(self):
        self.recommended_activity = 'Tour histórico por el centro de Manizales.'

    @Rule(CityActivity(city='manizales', climate='templado', budget='alto'))
    def manizales_mild_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Termales El Otoño.'
    
    @Rule(CityActivity(city='manizales', climate='nublado', budget='bajo'))
    def manizales_cloudy_low_budget(self):
        self.recommended_activity = 'Visitar la Catedral Basílica Metropolitana.'

    @Rule(CityActivity(city='manizales', climate='nublado', budget='medio'))
    def manizales_cloudy_medium_budget(self):
        self.recommended_activity = 'Recorrer el Palacio de Bellas Artes.'

    @Rule(CityActivity(city='manizales', climate='nublado', budget='alto'))
    def manizales_cloudy_high_budget(self):
        self.recommended_activity = 'Cena en el restaurante Termales El Otoño.'

class CityActivityApp:
    def __init__(self, master):
        self.master = master
        master.title("City Activity Recommender")

        self.label_city = ttk.Label(master, text="Ingresa la ciudad:")
        self.label_city.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        cities = ['Bogotá', 'Cali', 'Medellín', 'Cartagena', 'Barranquilla', 'Pereira', 'Manizales']
        self.city_entry = ttk.Combobox(master, values=cities, state="readonly")
        self.city_entry.grid(row=0, column=1, padx=10, pady=10)
        self.city_entry.set('Bogotá')

        self.label_climate = ttk.Label(master, text="Selecciona el clima:")
        self.label_climate.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        climates = ['soleado', 'lluvioso', 'nublado', 'templado']
        self.climate_combobox = ttk.Combobox(master, values=climates, state="readonly")
        self.climate_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.climate_combobox.set('soleado')

        self.label_budget = ttk.Label(master, text="Selecciona el presupuesto:")
        self.label_budget.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        budgets = ['bajo', 'medio', 'alto']
        self.budget_combobox = ttk.Combobox(master, values=budgets, state="readonly")
        self.budget_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.budget_combobox.set('bajo')

        self.recommend_button = ttk.Button(master, text="Recomendar Actividad", command=self.recommend_activity)
        self.recommend_button.grid(row=3, column=0, columnspan=2, pady=20)

    def recommend_activity(self):
        city = self.city_entry.get().lower()
        climate = self.climate_combobox.get().lower()
        budget = self.budget_combobox.get().lower()

        if city and climate and budget:
            engine = CityActivityExpert()
            engine.reset()
            engine.declare(CityActivity(city=city, climate=climate, budget=budget))
            engine.run()

            recommended_activity = engine.recommended_activity

            if recommended_activity:
                messagebox.showinfo("Recomendación", f"En {city.capitalize()}, te recomendamos la actividad: {recommended_activity}")
            else:
                messagebox.showwarning("Advertencia", "No se pudo determinar una actividad recomendada.")
        else:
            messagebox.showwarning("Error", "Completa todas las opciones antes de recomendar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CityActivityApp(root)
    root.mainloop()