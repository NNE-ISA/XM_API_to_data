# XM_API_to_data

El codigo ene ste repositorio permite a descargar información desde la API de XM utilizando Python, y la organiza en formato de tabla normalizada, por medio de la API se puede descargar información del sistema electríco Colombiano, organizada como se muestra en la siguiente tabla

<!--- -------------------------------------------------------------------------------------------------------
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
-->



<table class="default">
<tr><th>Item</th> <th>Frecuencia</th> <th>Variable</th> <th>Nombre</th></tr>
  
<tr><th rowspan="26">Sistema</th> <td rowspan="12">Horaria</td> <td>Generacion Ideal</td> <td>GeneIdea</td></tr>
<tr><td>Generacion Real                  </td> <td>Gene             </td></tr>
<tr><td>Demanda Comercial                </td> <td>DemaCome         </td></tr>
<tr><td>Precio de Bolsa Nacional         </td> <td>PrecBolsNaci     </td></tr>
<tr><td>Máximo Precio de Oferta Nacional </td> <td>MaxPrecOferNal   </td></tr>
<tr><td>Restricciones Aliviadas          </td> <td>RestAliv         </td></tr>
<tr><td>Ventas en Contratos Energía      </td> <td>VentContEner     </td></tr>
<tr><td>Compras en Contratos Energía     </td> <td>CompContEner     </td></tr>
<tr><td>Compras en Bolsa Nacional Energía</td> <td>CompBolsNaciEner </td></tr>
<tr><td>factor emision CO2e              </td> <td>factorEmisionCO2e</td></tr>
<tr><td>Importaciones Energía            </td> <td>ImpoEner         </td></tr>
<tr><td>Perdidas en Energia              </td> <td>PerdidasEner     </td></tr>

<tr><td rowspan="12">Diaria</td> <td>Aportes Energia</td>  <td>AporEner</td></tr>
<tr><td>Precio de Escasez de Activacion           </td>  <td>PrecEscaAct       </td></tr>
<tr><td>Remuneración Real Ind. Cargo Confiabilidad</td>  <td>RemuRealIndiv     </td></tr>
<tr><td>Precio Promedio Contratos Regulado        </td>  <td>PrecPromContRegu  </td></tr>
<tr><td>Precio Promedio Contratos NO Regulado     </td>  <td>PrecPromContNoRegu</td></tr>
<tr><td>Volumen Util Diario en Energia            </td>  <td>VoluUtilDiarEner  </td></tr>
<tr><td>Demanda del SIN                           </td>  <td>DemaSIN           </td></tr>
<tr><td>Capacidad Util Diaria en Energia          </td>  <td>CapaUtilDiarEner  </td></tr>
<tr><td>Media Historica Aportes                   </td>  <td>AporEnerMediHist  </td></tr>
<tr><td>FAZNI                                     </td>  <td>FAZNI             </td></tr>
<tr><td>PRONE                                     </td>  <td>PRONE             </td></tr>
<tr><td>FAER                                      </td>  <td>FAER              </td></tr>

<tr><td>Anual</td> <td>Listado de recursos térmicos CEN por mes</td> <td>CapEfecNeta</td></tr>

</table>
