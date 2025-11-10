/// <reference types="cypress" />

context('testes de login valido e invalido', () => {

    beforeEach(() => {
        cy.visit("https://www.saucedemo.com")
    });


    it('Login válido - Usuário Padrão', () => {
        cy.get('#user-name').type('standard_user')
        cy.get('#password').type('secret_sauce')
        cy.get('#login-button').click()
        cy.url().should('include', 'inventory.html')
    });

});