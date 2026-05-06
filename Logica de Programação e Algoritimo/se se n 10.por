programa {
  funcao inicio() {
    inteiro lado1,lado2,lado3

    escreva("digite lado1")
    leia(lado1)

    escreva("digite lado2")
    leia(lado2)

    escreva("digite lado3")
    leia(lado3)

    se(lado1 == lado2 e lado1 == lado3 e lado2 == lado3){
      escreva("equilátero")
    }

     se(lado1 == lado2 ou lado2 == lado3 e lado3 != lado1  ){
      escreva("isósceles")
     }
     se(lado1 != lado2 e lado2 != lado3 != lado1){
      
     }

      
    }
  }


}
