programa {
  funcao inicio() {
    cadeia operacao
    inteiro num1,num2
    real resultado

    escreva("digite a operação(+,-,*,/):")
    leia(operacao) 

    escreva("digite o primeiro numeroa:")
    leia(num1)

    escreva("digite o segundo numero")
    leia(num2)

    se(operacao == "+"){
      resultado = num1 + num2
    }
    senao se(operacao =="*"){
      resultado = num1 * num2
    }
    senao se(operacao == ("-")){
      resultado = num1 - num2
    }
    senao se (operacao == ("/")){
      resultado = num1 / num2
    }
    senao{
      escreva("operacao invalida!")
    }
    escreva("o resultado é :", resultado)

  }
}
