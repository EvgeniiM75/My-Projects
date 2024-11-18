/// <reference types="cypress" />

const email = "Ваша почта";
const password = "Ваш пароль";


describe("Citilink tests", () => {
  Cypress.on('uncaught:exception', (err) => {
    // Игнорировать ошибки, связанные с google_tag_manager
    if (err.message.includes('google_tag_manager is not defined')) {
      return false; // Предотвращает сбой теста
    }

  });

  it("By", () => {
    // Переходим на сайт
    cy.visit("https://www.citilink.ru/");

    // Настроим размер окна браузера
    cy.viewport(1920, 1080);
    // Принимаем куки
    cy.get(".app-catalog-1aoqav5 > .e4uhfkv0 > .app-catalog-1xdhyk6").click();

    // Нажать "Войти"
    cy.get(".eequ4qc0").click();
    cy.wait(1000);

    // Нажать "Войти по паролю"
    cy.get(".app-catalog-1oipxdc-Button--StyledSwitcherButton")
      .click();
    cy.wait(1000);

    // Ввести email
    cy.get(".eoyvx5n0 > .app-catalog-hyxlzm > .app-catalog-1u9ewb3")
      .should("be.visible")
      .type(email);

    // Ввести пароль
    cy.get(".e5wmf4n0 > .app-catalog-hyxlzm > .app-catalog-1u9ewb3")
      .should("be.visible")
      .type(password);

    // Нажать "Войти"
    cy.get(".app-catalog-xdsehz-Action--StyledActions > .e4uhfkv0")
      .click();
    cy.wait(2000);

    // Выполнить поиск «iphone 16»
    cy.get(".e1cpn7530 > .app-catalog-hyxlzm > .app-catalog-1u9ewb3")
      .type("iphone 16");
    cy.get('.app-catalog-1d9cswg > [type="submit"]')
      .click();
    cy.wait(1000);

    // Перейти на страницу смартфона
    cy.get(":nth-child(1) > .e1l56t9a0 > .app-catalog-165w3p6 > .app-catalog-5bve6v > .app-catalog-shrvo4 > .app-catalog-9gnskf")
      .click();

    // Нажать "Оформить заказ"
    cy.get(".e11w80q30").click();
    cy.wait(1000);

    // Нажать "Перейти к оформлению"
    cy.get(".eqwt6oe0 > .e4uhfkv0").click();
    cy.wait(1000);

    // Нажать "Выберите способ оплаты"
    cy.get(".efo328f0 > :nth-child(2)").click();
    //cy.get('label[class="eddme6n0 e1twwlg30 css-u1bjlw e1amf8g0"][1]').click();
    cy.wait(1000);

    // Нажать "Оформить заказ"
    cy.get(".e1jq023s0").should("be.visible").click();
    cy.wait(1000);

  });
});


