t = parse(Int, readline())

for i in 1:t
        N = parse(Int, readline())
        v = [ parse(Int, x) for x in split(readline())]

        count = 0
        record = -1
        for s in 1:N
                if v[s] > record && (s == N || v[s] > v[s+1])
                        count += 1
                end #if1
                record = max(record, v[s])
        end

    println("Case #$i: $count")

end
