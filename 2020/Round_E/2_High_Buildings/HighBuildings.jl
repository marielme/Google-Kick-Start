t = parse(Int, readline())

for i in 1:t
    N, A, B, C = [ parse(Int, x) for x in split(readline())]

    print("Case #",i,":")

    if A+B-C > N || (A+B-C == 1 && N>=2)
        println(" IMPOSSIBLE")
    else
        if N == 1
            println(" 1")
        elseif N == 2
            if C == 2
                println(" 2 2") 
            elseif B == 2
                println(" 2 1") 
            elseif A == 2
                println(" 1 2") 
            else
                println(" IMPOSSIBLE") 
            end
        else
            ans = []
            for j in 1:(A-C)
                append!(ans,2)
            end
            for j in 1:C
                append!(ans,3)
            end
            hide = N-A-B+C
            if hide > 0
                for j in 1:hide
                    insert!(ans,2, 1)
                end
            end    
            for j in 1:(B-C)
                append!(ans,2)
            end
            for j in 1:length(ans)-1
                print(" ",ans[j])
            end
            println(" ",ans[end])
        end
    end

end
