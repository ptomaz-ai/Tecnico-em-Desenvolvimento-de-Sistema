programa {
  funcao inicio() {
    inteiro idade
    
    escreva("digite sua idade ")
    leia(idade)

    se(idade>=0 e idade<=12){
      escreva("Criança")
    }
    se(idade>=13 e idade<=17){
escreva("Adolecente")
      
    }
    se(idade>=18 e idade<=59){
      escreva("Adluto")
    }
    se(idade>=60 e idade<=100){
      escreva("Idoso")
    }
  }
}
