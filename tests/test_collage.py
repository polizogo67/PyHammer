from hammer.utils import collage_arange

def test_collage() -> None:

    r:int = 0
    c:float = 0

    r, c = collage_arange(5, 460, 380)

    print( f"RxC: {r,c}" ) # (3, 2)
    print(f"Collage Shape: {r}x{c}, Final Shape: {460*c}x{380*r}") # 920x1140
