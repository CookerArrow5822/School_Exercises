triangleArea :: Float -> Float -> Float -> Float

triangleArea a b c = 
    if a^2 + b^2 <= c^2
        then error "Not a triangle"
        else sqrt(s * ((s - a) * (s - b) * (s - c)))
    where
        s = (a + b + c) / 2
