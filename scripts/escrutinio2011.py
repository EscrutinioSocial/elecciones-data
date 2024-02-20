from uuid import uuid4
from selenium import webdriver

from selenium.webdriver.support.ui import Select
import csv


URL = "https://www.justiciacordoba.gob.ar/Jel/Contenido/escrutinios.aspx"


def main():
    # init driver
    options = webdriver.FirefoxOptions()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(URL)
    xpath_list = "/html/body/form/div[3]/div[2]/div/div/div/div/div[2]/div/div[3]/*"
    # filter href
    elements = driver.find_elements_by_xpath(xpath_list)
    links = []
    # find a with href in elements

    for element in elements:
        try:
            a = element.find_element_by_tag_name("a")
            links.append(a.get_attribute("href"))
        except:
            pass

    """
        links[0] => 2023
        links[1] => 2019
        links[2] => 2015
        links[3] => 2011
        links[4] => 2007
        years = ["20230514", "20190512", "20150705", "20110807", "20070902"]
    """
    # here I select the 4th link because it is the one that contains the 2011 election
    links = [links[3]]
    years = ["20110807"]

    counter = 0

    # starts scraping per each year selected
    for link in links:
        driver.get(link)
        # swich to topFrame
        driver.switch_to.frame("topFrame")

        # by localidad
        localidades = driver.find_element_by_id("cmbLocalidadesTodos")
        localidades_select = Select(localidades)
        list_localidades = localidades.find_elements_by_tag_name(
            "option")

        for localidad in list_localidades:
            ltext = localidad.text
            localidades_select.select_by_visible_text(ltext)
            cargos = driver.find_element_by_id("cmbCargos")
            cargos_select = Select(cargos)
            list_cargos = cargos.find_elements_by_tag_name("option")
            for cargo in list_cargos:
                cotext = cargo.text

                cargos_select.select_by_visible_text(cotext)
                mostrar_button = driver.find_element_by_id(
                    "cmdMostrar")

                mostrar_button.click()
                # find frame with name "mainFrame"
                # get back to top frame
                driver.switch_to.default_content()
                driver.switch_to.frame("mainFrame")
                table = driver.find_elements_by_tag_name("table")[0]

                try:
                    with open("LOCALIDAD_"+ltext+"_"+cotext+"_"+str(years[counter])+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)
                except OSError as error:
                    print(error)
                    print(ltext, cotext)
                    with open(str(uuid4)+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)

                except Exception as error:
                    print(error)
                driver.switch_to.default_content()
                driver.switch_to.frame("topFrame")

        # by circuito
        circuitos = driver.find_element_by_id("cmbCircuitosTodos")
        circuitos_select = Select(circuitos)
        list_circuitos = circuitos.find_elements_by_tag_name("option")

        for circuito in list_circuitos:
            ctext = circuito.text
            circuitos_select.select_by_visible_text(ctext)

            cargos = driver.find_element_by_id("cmbCargos")
            cargos_select = Select(cargos)
            list_cargos = cargos.find_elements_by_tag_name("option")

            for cargo in list_cargos:
                cotext = cargo.text

                cargos_select.select_by_visible_text(cotext)
                mostrar_button = driver.find_element_by_id(
                    "cmdMostrar")

                mostrar_button.click()
                # find frame with name "mainFrame"
                # get back to top frame
                driver.switch_to.default_content()
                driver.switch_to.frame("mainFrame")
                table = driver.find_elements_by_tag_name("table")[0]

                try:
                    with open("CIRCUITO_"+ctext+"_"+cotext+"_"+str(years[counter])+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)
                except OSError as error:
                    print(error)
                    print(ctext, cotext)
                    with open(str(uuid4)+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)
                except Exception as error:
                    print(error)
                driver.switch_to.default_content()
                driver.switch_to.frame("topFrame")

        # by seccion

        secciones = driver.find_element_by_id("cmbSecciones")
        secciones_select = Select(secciones)
        list_secciones = secciones.find_elements_by_tag_name("option")

        for seccion in list_secciones:
            stext = seccion.text
            secciones_select.select_by_visible_text(stext)

            cargos = driver.find_element_by_id("cmbCargos")
            cargos_select = Select(cargos)
            list_cargos = cargos.find_elements_by_tag_name("option")

            for cargo in list_cargos:
                cotext = cargo.text

                cargos_select.select_by_visible_text(cotext)
                mostrar_button = driver.find_element_by_id(
                    "cmdMostrar")

                mostrar_button.click()

                # get back to top frame
                driver.switch_to.default_content()
                driver.switch_to.frame("mainFrame")
                table = driver.find_elements_by_tag_name("table")[0]

                try:
                    with open("SECCION_"+stext+"_"+cotext+"_"+str(years[counter])+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)
                except OSError as error:
                    print(error)
                    print(stext, cotext)
                    with open(str(uuid4)+".csv", 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        rows = table.find_elements_by_tag_name('tr')
                        rows = rows[4:]

                        # get text from rows

                        for row in rows:
                            rtext = [d.text for d in list(
                                filter(lambda x: x.text != "", row.find_elements_by_tag_name('td')))]
                            if len(rtext) > 0:
                                wr.writerow(rtext)
                except Exception as error:
                    print(error)
                driver.switch_to.default_content()
                driver.switch_to.frame("topFrame")
        counter += 1


if __name__ == "__main__":
    main()
