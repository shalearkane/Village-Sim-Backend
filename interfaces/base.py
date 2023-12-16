class Base:
    def __init__(self, roadDistance, residentialDistance, hospitalDistance, agriculturalDistance, 
                 commercialDistance, industrialDistance, schoolDistance, healthDistance, 
                 sewageTreatmentDistance, waterBodyDistance):
        self.roadDistance = roadDistance
        self.residentialDistance = residentialDistance
        self.hospitalDistance = hospitalDistance
        self.agriculturalDistance = agriculturalDistance
        self.commercialDistance = commercialDistance
        self.industrialDistance = industrialDistance
        self.schoolDistance = schoolDistance
        self.healthDistance = healthDistance
        self.sewageTreatmentDistance = sewageTreatmentDistance
        self.waterBodyDistance = waterBodyDistance
    
    def to_dict(self):
        return {
            "roadDistance": self.roadDistance,
            "residentialDistance": self.residentialDistance,
            "hospitalDistance": self.hospitalDistance,
            "agriculturalDistance": self.agriculturalDistance,
            "commercialDistance": self.commercialDistance,
            "industrialDistance": self.industrialDistance,
            "schoolDistance": self.schoolDistance,
            "healthDistance": self.healthDistance,
            "sewageTreatmentDistance": self.sewageTreatmentDistance,
            "waterBodyDistance": self.waterBodyDistance
        }