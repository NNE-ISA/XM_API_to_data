# XM_API_to_data

El codigo ene ste repositorio permite a descargar información desde la API de XM utilizando Python, y la organiza en formato de tabla normalizada, por medio de la API se puede descargar información del sistema electríco Colombiano, organizada como se muestra en la siguiente tabla

-------------------------------------------------------------------------------------------------------
|     ITEM       |  FRECUENCIA |     INFORMACIÓN                                |  NOMBRE             |
|----------------|-------------|------------------------------------------------|---------------------|
|                |             | Generacion Ideal                               |GeneIdea             |
|                |             | Generacion Real                                |Gene                 |
|                |             | Demanda Comercial                              |DemaCome             |
|                |             | Precio de Bolsa Nacional                       |PrecBolsNaci         |
|                |             | Máximo Precio de Oferta Nacional               |MaxPrecOferNal       |
|                |   Horaria   | Restricciones Aliviadas                        |RestAliv             |
|                |             | Ventas en Contratos Energía                    |VentContEner         |
|                |             | Compras en Contratos Energía                   |CompContEner         |
|                |             | Compras en Bolsa Nacional Energía              |CompBolsNaciEner     |                                              
|                |             | factor emision CO2e                            |factorEmisionCO2e    |
|                |             | Importaciones Energía                          |ImpoEner             |
|                |             | Perdidas en Energia                            |PerdidasEner         |
|    Sistema     |------------------------------------------------------------------------------------|
|                |   Diaria    | Aportes Energia                                | AporEner            |
|                |             | Precio de Escasez de Activacion                | PrecEscaAct         |
|                |             | Remuneración Real Ind. Cargo Confiabilidad     | RemuRealIndiv       |
|                |             | Precio Promedio Contratos Regulado             | PrecPromContRegu    |
|                |             | Precio Promedio Contratos NO Regulado          | PrecPromContNoRegu  |
|                |             | Volumen Util Diario en Energia                 | VoluUtilDiarEner    |
|                |             | Demanda del SIN                                | DemaSIN             |
|                |             | Capacidad Util Diaria en Energia               | CapaUtilDiarEner    |
|                |             | Media Historica Aportes                        | AporEnerMediHist    |
|                |             | FAZNI                                          | FAZNI               |
|                |             | PRONE                                          | PRONE               |
|                |             | FAER                                           | FAER                |
|                |------------------------------------------------------------------------------------|
|                |   Anual     | Listado de recursos térmicos CEN por mes       | CapEfecNeta         |
|----------------|------------------------------------------------------------------------------------|
|                |             | Generación Ideal                               | GeneIdea            |
|                |             | Generación Real                                | Gene                |
|                |             | Cosumo de combustible Aprox. Factor de Emisión | ConsCombustibleMBTU |
|                |   Horaria   | Precio de Oferta del Despacho                  | PrecOferDesp        |
|    Recursos    |             | Emisiones CO2e                                 | EmisionesCO2Eq      |
|                |             | Generación Seguridad                           | GeneSeguridad       |
|                |             | Generación Fuera de Merito                     | GeneFueraMerito     |
|                |------------------------------------------------------------------------------------|
|                |   Diaria    | Obligaciones de Energía Firme                  | ObligEnerFirme      |
|-----------------------------------------------------------------------------------------------------|
|                |             | Consumo Comb Aprox                             | ConsCombAprox       |
|    Recursos    |   Horaria   | Emisiones CO                                   | EmisionesCO2        |
|   Combinados   |             | Emisiones CH                                   | EmisionesCH4        |
|                |             | Emisiones N2                                   | EmisionesN2O        |
|-----------------------------------------------------------------------------------------------------|
|                |             | Demanda Comercial                              | DemaCome            |
|                |             | Ventas en Contratos Energía                    | VentContEner        |
|    Agentes     |   Horaria   | Compras en Contratos Energía                   | CompContEner        |
|                |             | Compras en Bolsa Nacional Energía              | CompBolsNaciEner    |
|                |             | Demanda por Operador de Red                    | DemaOR              |
|-----------------------------------------------------------------------------------------------------|
|      Rios      |   Diaria    | Aportes Energia                                | AporEner            |
|                |             | Media Historica Aportes                        | AporEnerMediHist    |
|-----------------------------------------------------------------------------------------------------|
|    Embalses    |   Diaria    | Volumen Util Diario en Energia                 | VoluUtilDiarEner    |
|                |             | Capacidad Util Diaria en Energia               | CapaUtilDiarEner    |
|-----------------------------------------------------------------------------------------------------|
|     Areas      |   Diaria    | Demanda No Atendida Programada por Área        | DemaNoAtenProg      |
|                |             | Demanda No Atendida No Programada por Área     | DemaNoAtenNoProg    |
|-----------------------------------------------------------------------------------------------------|
|   Subareas     |   Diaria    | Demanda No Atendida Programada por Área        | DemaNoAtenProg      |
|                |             | Demanda No Atendida No Programada por Área     | DemaNoAtenNoProg    |



<table class="default">
<tr>
<th></th>
<th>Básico</th>
<th>Completo</th>
</tr>
<tr>
<th>Instalación</th>
<td rowspan="2">Gratis!</td>
<td>$49.99</td>
</tr>

<tr>
<th>Primer año</th>
<td>$19.99</td>
</tr>
<tr>

<th>Segundo año</th>
<td>$9.99</td>
<td>$29.99</td>

</tr>
</table>
