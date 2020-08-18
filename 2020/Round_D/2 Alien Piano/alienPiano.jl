t = parse(Int, readline())

for i in 1:t
        k = parse(Int, readline())
        a = [ parse(Int, j) for j in split(readline())]

        v = [a[i] for i = 1:k if i == 1 || a[i - 1] != a[i]]

        upCount = 0
        downCount = 0
        violations = 0

        for i = 2:length(v)
          if v[i] > v[i - 1]
            upCount += 1
            downCount = 0
          else
            downCount += 1
            upCount = 0
          end #if
          if upCount > 3 || downCount > 3
            violations += 1
            upCount = downCount = 0
          end #if
        end #for

println("Case #$i: $violations")

end
