from ExtAPIs.models import Prime, Factor, PrimeFactorModel, IntToBinaryModel, BinaryToIntModel, FibonacciModel, ArithSeriesModel,\
    GeoSeriesModel, ProjectilePath2DModel

def all_prime_objects():
    return Prime.objects.all()

def all_factor_objects():
    return Factor.objects.all()

def all_prime_factor_objects():
    return PrimeFactorModel.objects.all()

def all_int_to_bin_objects():
    return IntToBinaryModel.objects.all()

def all_bin_to_int_objects():
    return BinaryToIntModel.objects.all()

def all_fibonacci_objects():
    return FibonacciModel.objects.all()

def all_arith_series_objects():
    return ArithSeriesModel.objects.all()

def all_geo_series_objects():
    return GeoSeriesModel.objects.all()

def all_projectile_path2d_objects():
    return ProjectilePath2DModel.objects.all()

def delete_objs(list_of_objects=None):
    for object in list_of_objects:
        print(f"Deleting {object.__dict__}")
        object.delete()

def clear_models():
    list_of_objects = []

    list_of_objects.extend(all_prime_objects())
    list_of_objects.extend(all_factor_objects())
    list_of_objects.extend(all_prime_factor_objects())
    list_of_objects.extend(all_int_to_bin_objects())
    list_of_objects.extend(all_bin_to_int_objects())
    list_of_objects.extend(all_fibonacci_objects())
    list_of_objects.extend(all_arith_series_objects())
    list_of_objects.extend(all_geo_series_objects())
    list_of_objects.extend(all_projectile_path2d_objects())

    delete_objs(list_of_objects)

def main():
    clear_models()

if __name__=="__main__":
    main()