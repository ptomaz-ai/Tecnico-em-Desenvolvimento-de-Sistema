programa {
  funcao inicio() {
    inteiro valor_compra
    cadeia possui_cupom

    escreva("qual o valor da compra?")
    leia(valor_compra)

    escreva("possui_cupom")
    leia(possui_cupom)

    se(valor_compra>200 ou possui_cupom=="sim"){
      escreva("você ganho desconto de 15%!")
    }
    senao{
      escreva("infelismente você não ganho cupom")
    }

  }
}
