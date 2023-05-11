def eq(a):
    aOr, varRpp, varR = a, "", ""

    for j in range(len(a)):
        if a[j] not in varRpp and a[j] not in "+*()":
            varRpp += a[j]
        elif a[j] in varRpp:
            a = a[:j - 1] + a[j - 1:j + 1].replace(a[j - 1:j + 1], "") + a[j + 2:]

    for i in range(2 ** (len(a) // 2 + 1)):
        if i < len(a) - 1:
            for j in range((len(a) // 2 + 1) - len(bin(i)) // 2): varR += "0"

        varR += str(bin(i))

        varR = varR.replace("0b", "")

    ctt, jaFeito, a = 0, "", aOr

    print(varRpp + "*")

    for r in range(2 ** (len(varRpp))):

        jaFeito, aOr = "", a

        for q in range(len(aOr)):  # trabalhar com o original
            if aOr[q] not in "()+*" and aOr[q] not in jaFeito:
                aOr = aOr.replace(aOr[q], varR[r + ctt])

                jaFeito += aOr[q]

                print(aOr[q])

                ctt += 1

        ctt -= 1

        if eval(aOr) != 0:
            print("r:1")
        else:
            print("r:0")
