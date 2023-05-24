import propar
import serial
import time
import valves4 as vl
from logger import *

# Master address for stablishing communication with the E-8000 and Flow-SMS
master = propar.master('COM5', 38400)

# Fuction that set the flows in the Flow-SMS unit
# By indicating the inert gas flow in the mix or pulse line MFC
# the gas settings are automatically changed for using the proper calibration curve for each gas
def flowsms_setpoints(
        CO2 = None, CO = None, CH4 = None, 
        H2 = None, D2 = None, O2 = None, He_mix = None, 
        He_pulses = None, Ar_pulses = None, 
        Ar_mix = None, N2_mix = None, N2_pulses = None):

  # Node ID values assigned in the MFCs configuration
  ID_P_mix = 3
  ID_CO2 = 4
  ID_carrier_pulses = 5
  ID_CO = 6
  ID_carrier_mix = 7
  ID_P_pulses = 8
  ID_CH4 = 9
  ID_H2 = 10
  ID_O2 = 11
  
  # Calibration curve IDs for inert gas MFCs
  cal_He = 0
  cal_Ar = 1
  cal_N2 = 2
  
  # Flow setpoint instructions for the Flow-SMS mass flow controllers
  # If non flow is indicated for an specific gas, a zero flow will be
  # set to its corresponding MFC
  # Flows are converted to a number base 32000 to be read by the MFCs
  if CO2 == None:
    flow_co2 = 0
    data_co2 = flow_co2
    params_co2 = [{'node': ID_CO2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co2}]
    status = master.write_parameters(params_co2)
  else:
    flow_co2 = float(CO2) # Number from 0 - 30.00 sccm
    if flow_co2 < 0.6:
      print('CO2 flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_co2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_co2 > 30:
      print('CO2 flow higher than maximum 30 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_co2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_co2 = int(flow_co2*(32000/30))
    params_co2 = [{'node': ID_CO2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co2}]
    status = master.write_parameters(params_co2)
    
  if CO == None:
    flow_co = 0
    data_co = flow_co
    params_co = [{'node': ID_CO, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co}]
    status = master.write_parameters(params_co)
  else:
    flow_co = float(CO) # Number from 0 - 30.00 sccm
    if flow_co < 0.6:
      print('CO flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_co = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_co > 30:
      print('CO flow higher than maximum 30 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_co = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_co = int(flow_co*(32000/30))
    params_co = [{'node': ID_CO, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co}]
    status = master.write_parameters(params_co)
    
  if CH4 == None:
    flow_ch4 = 0
    data_ch4 = flow_ch4
    params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
    status = master.write_parameters(params_ch4)
  else:
    flow_ch4 = float(CH4) # Number from 0 - 30.00 sccm
    if flow_ch4 < 0.6:
      print('CH4 flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_ch4 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_ch4 > 30:
      print('CH4 flow higher than maximum 30 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_ch4 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_ch4 = int(flow_ch4*(32000/30))
    params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
    status = master.write_parameters(params_ch4)
    
  if CH4 == None:#new
    if D2 == None:
      flow_ch4 = 0
      data_ch4 = flow_ch4
      params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
      status = master.write_parameters(params_ch4)
    else:
      flow_ch4 = float(D2) # Number from 0 - 30.00 sccm
      flow_ch4 = flow_ch4 /1.310190514
      if flow_ch4 < 0.6:
        print('CH4 flow lower than minimum 0.6 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_ch4 = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      elif flow_ch4 > 30:
        print('CH4 flow higher than maximum 30 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_ch4 = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      else:
        pass
      data_ch4 = int(flow_ch4*(32000/30))
      params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
      status = master.write_parameters(params_ch4)
    
  if H2 == None:
    flow_h2 = 0
    data_h2 = flow_h2
    params_h2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_h2}]
    status = master.write_parameters(params_h2)
  else:
    vl.feed_H2()
    flow_h2 = float(H2) # Number from 0 - 30.00 sccm
    if flow_h2 < 0.6:
      print('H2 flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_h2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_h2 > 30:
      print('H2 flow higher than maximum 30 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_h2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_h2 = int(flow_h2*(32000/30))
    params_h2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_h2}]
    status = master.write_parameters(params_h2)
    
  # if D2 == None:
    # flow_d2 = 0
    # data_d2 = flow_d2
    # params_d2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_d2}]
    # status = master.write_parameters(params_d2)
  # else:
    # vl.feed_D2()
    # flow_d2 = float(D2) # Number from 0 - 30.00 sccm
    # flow_d2 = flow_d2 * 0.99433 # Flow corrected by D2 calibration factor
    # if flow_d2 < 0.6:
      # print('D2 flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # flow_d2 = float(input('Enter new flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    # elif flow_d2 > 30:
      # print('D2 flow higher than maximum 30 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # flow_d2 = float(input('Enter new flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    # else:
      # pass
    # data_d2 = int(flow_d2*(32000/30))
    # params_d2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_d2}]
    # status = master.write_parameters(params_d2)
    
  if O2 == None:
    flow_o2 = 0
    data_o2 = flow_o2
    params_o2 = [{'node': ID_O2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_o2}]
    status = master.write_parameters(params_o2)
  else:
    flow_o2 = float(O2) # Number from 0 - 30.00 sccm
    if flow_o2 < 0.6:
      print('O2 flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_o2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_o2 > 30:
      print('O2 flow higher than maximum 30 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_o2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_o2 = int(flow_o2*(32000/30))
    params_o2 = [{'node': ID_O2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_o2}]
    status = master.write_parameters(params_o2)
    
  if He_mix == None and Ar_mix == None:
    flow_he_mix = 0
    data_he_mix = flow_he_mix
    params_he_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_mix}]
    status = master.write_parameters(params_he_mix)
  else:
    try:
      flow_he_mix = float(He_mix) # Number from 0 - 60.00 sccm
      vl.carrier_He_mix()
      if flow_he_mix < 0.6:
        print('He mixing flow lower than minimum 0.6 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_he_mix = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      elif flow_he_mix > 60:
        print('He mixing flow higher than maximum 60 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_he_mix = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      else:
        pass
      data_he_mix = int(flow_he_mix*(32000/60))
      params_he_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                       {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_mix}]
      status = master.write_parameters(params_he_mix)
    except:
      He_mix = None
    
    
  try:
    flow_he_pulses = float(He_pulses) # Number from 0 - 60.00 sccm
    vl.carrier_He_pulses()
    if flow_he_pulses < 0.6:
      print('He pulses flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_he_pulses = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_he_pulses > 60:
      print('He pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_o2 = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_he_pulses = int(flow_he_pulses*(32000/60))
    params_he_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_pulses}]
    status = master.write_parameters(params_he_pulses)
  except:
    He_pulses = None
    if He_pulses == None and Ar_pulses == None:
      data_he_pulses = 0
      params_he_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                       {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_pulses}]
      status = master.write_parameters(params_he_pulses)
    
  if Ar_mix == None and He_mix == None:
    flow_ar_mix = 0
    data_ar_mix = flow_ar_mix
    params_ar_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_mix}]
    status = master.write_parameters(params_ar_mix)
  else:
    try:
      flow_ar_mix = float(Ar_mix) # Number from 0 - 60.00 sccm
      vl.carrier_Ar_mix()
      if flow_ar_mix < 0.6:
        print('Ar mixing flow lower than minimum 0.6 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_ar_mix = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      elif flow_ar_mix > 60:
        print('Ar mixing flow higher than maximum 60 sccm')
        iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
        if iterval == 'Yes':
          flow_ar_mix = float(input('Enter new flow: '))
        elif iterval == 'No':
          raise SystemExit
      else:
        pass
      data_ar_mix = int(flow_ar_mix*(32000/60))
      params_ar_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                       {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_mix}]
      status = master.write_parameters(params_ar_mix)
    except:
      Ar_mix = None
    
  try:
    flow_ar_pulses = float(Ar_pulses) # Number from 0 - 60.00 sccm
    vl.carrier_Ar_pulses()
    if flow_ar_pulses < 0.6:
      print('Ar pulses flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_ar_pulses = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_ar_pulses > 60:
      print('Ar pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_ar_pulses = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_ar_pulses = int(flow_ar_pulses*(32000/60))
    params_ar_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_pulses}]
    status = master.write_parameters(params_ar_pulses)
  except:
    Ar_pulses = None
    if He_pulses == None and Ar_pulses == None:
      data_ar_pulses = 0
      params_ar_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                       {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_pulses}]
      status = master.write_parameters(params_ar_pulses)
    
  try:
    flow_n2_mix = float(N2_mix) # Number from 0 - 60.00 sccm
    if flow_n2_mix < 0.6:
      print('N2 mixing flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_n2_mix = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_n2_mix > 60:
      print('N2 mixing flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_n2_mix = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_n2_mix = int(flow_n2_mix*(32000/60))
    params_n2_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_N2},
                     {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_n2_mix}]
    status = master.write_parameters(params_n2_mix)    
  except:
    N2_mix = None
    
  try:
    flow_n2_pulses = float(N2_pulses) # Number from 0 - 60.00 sccm
    if flow_n2_pulses < 0.6:
      print('N2 pulses flow lower than minimum 0.6 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_n2_pulses = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    elif flow_n2_pulses > 60:
      print('N2 pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_n2_pulses = float(input('Enter new flow: '))
      elif iterval == 'No':
        raise SystemExit
    else:
      pass
    data_n2_pulses = int(flow_n2_pulses*(32000/60))
    params_n2_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_N2},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_n2_pulses}]
    status = master.write_parameters(params_n2_pulses)
  except:
    N2_pulses = None      


# Fuction that set the flows in the Flow-SMS unit based on percentage values
# By indicating the inert gas flow in the mix or pulse line MFC
# the gas settings are automatically changed for using the proper calibration curve for each gas
def flowsms_setpoints_percent(
        CO2 = None, CO = None, CH4 = None, 
        H2 = None, D2 = None, O2 = None, 
        totalflow_He_mix = None, totalflow_He_pulses = None, 
        totalflow_Ar_pulses = None, totalflow_Ar_mix = None, 
        totalflow_N2_mix = None, totalflow_N2_pulses = None):

  # Node ID values assigned in the MFCs configuration
  ID_P_mix = 3
  ID_CO2 = 4
  ID_carrier_pulses = 5
  ID_CO = 6
  ID_carrier_mix = 7
  ID_P_pulses = 8
  ID_CH4 = 9
  ID_H2 = 10
  ID_O2 = 11
  
  # Calibration curve IDs for inert gas MFCs
  cal_He = 0
  cal_Ar = 1
  cal_N2 = 2
  
  # Flow setpoint instructions for the Flow-SMS mass flow controllers
  # If non flow is indicated for an specific gas, no instruntion will be
  # send to its corresponding MFC
  # Flows are converted to a number base 32000 to be read by the MFCs
  if CO2 == None:
    flow_co2 = 0
    data_co2 = flow_co2
    params_co2 = [{'node': ID_CO2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co2}]
    status = master.write_parameters(params_co2)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    co2_perc = float(CO2) # Number from 0 - 100 %
    flow_co2 = (co2_perc * total_flow_mix)/100
    while flow_co2 < 0.6:
      co2_min = (0.6 * 100)/total_flow_mix
      print('CO2 concentration lower than minimum {}%'.format(co2_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        co2_perc = float(input('Enter new concentration: '))
        flow_co2 = (co2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_co2 > 30:
      co2_max = (30 * 100)/total_flow_mix
      print('CO2 concentration higher than maximum {}%'.format(co2_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        co2_perc = float(input('Enter new concentration: '))
        flow_co2 = (co2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_co2 = int(flow_co2*(32000/30))
    params_co2 = [{'node': ID_CO2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co2}]
    status = master.write_parameters(params_co2)

  if CO == None:
    flow_co = 0
    data_co = flow_co
    params_co = [{'node': ID_CO, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co}]
    status = master.write_parameters(params_co)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    co_perc = float(CO) # Number from 0 - 100 %
    flow_co = (co_perc * total_flow_mix)/100
    while flow_co < 0.6:
      co_min = (0.6 * 100)/total_flow_mix
      print('CO concentration lower than minimum {}%'.format(co_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        co_perc = float(input('Enter new concentration: '))
        flow_co = (co_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_co > 30:
      co_max = (30 * 100)/total_flow_mix
      print('CO concentration higher than maximum {}%'.format(co_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        co_perc = float(input('Enter new concentration: '))
        flow_co = (co_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_co = int(flow_co*(32000/30))
    params_co = [{'node': ID_CO, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_co}]
    status = master.write_parameters(params_co)
    
  if CH4 == None:
    flow_ch4 = 0
    data_ch4 = flow_ch4
    params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
    status = master.write_parameters(params_ch4)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    ch4_perc = float(CH4) # Number from 0 - 100 %
    flow_ch4 = (ch4_perc * total_flow_mix)/100
    while flow_ch4 < 0.6:
      ch4_min = (0.6 * 100)/total_flow_mix
      print('CH4 concentration lower than minimum {}%'.format(ch4_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        ch4_perc = float(input('Enter new concentration: '))
        flow_ch4 = (ch4_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_ch4 > 30:
      ch4_max = (30 * 100)/total_flow_mix
      print('CH4 concentration higher than maximum {}%'.format(ch4_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        ch4_perc = float(input('Enter new concentration: '))
        flow_ch4 = (ch4_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_ch4 = int(flow_ch4*(32000/30))
    params_ch4 = [{'node': ID_CH4, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ch4}]
    status = master.write_parameters(params_ch4)
    
  if H2 == None:
    flow_h2 = 0
    data_h2 = flow_h2
    params_h2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_h2}]
    status = master.write_parameters(params_h2)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    vl.feed_H2()
    h2_perc = float(H2) # Number from 0 - 100 %
    flow_h2 = (h2_perc * total_flow_mix)/100
    while flow_h2 < 0.6:
      h2_min = (0.6 * 100)/total_flow_mix
      print('H2 concentration lower than minimum {}%'.format(h2_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        h2_perc = float(input('Enter new concentration: '))
        flow_h2 = (h2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_h2 > 30:
      h2_max = (30 * 100)/total_flow_mix
      print('H2 concentration higher than maximum {}%'.format(h2_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        h2_perc = float(input('Enter new concentration: '))
        flow_h2 = (h2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_h2 = int(flow_h2*(32000/30))
    params_h2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_h2}]
    status = master.write_parameters(params_h2)
    
  if D2 == None:
    flow_d2 = 0
    data_d2 = flow_d2
    params_d2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_d2}]
    status = master.write_parameters(params_h2)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    vl.feed_D2()
    d2_perc = float(D2) # Number from 0 - 100 %
    flow_d2 = (d2_perc * total_flow_mix)/100
    flow_d2 = flow_d2 * 0.99433
    while flow_d2 < 0.6:
      d2_min = (0.6 * 100)/total_flow_mix
      print('D2 concentration lower than minimum {}%'.format(d2_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        d2_perc = float(input('Enter new concentration: '))
        flow_d2 = (d2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_d2 > 30:
      d2_max = (30 * 100)/total_flow_mix
      print('D2 concentration higher than maximum {}%'.format(d2_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        d2_perc = float(input('Enter new concentration: '))
        flow_d2 = (d2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_d2 = int(flow_d2*(32000/30))
    params_d2 = [{'node': ID_H2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_d2}]
    status = master.write_parameters(params_d2)
    
  if O2 == None:
    flow_o2 = 0
    data_o2 = flow_o2
    params_o2 = [{'node': ID_O2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_o2}]
    status = master.write_parameters(params_o2)
  else:
    try:
      total_flow_mix = float(totalflow_He_mix) # Number in sccm
    except:
      totalflow_He_mix = None
    try:
      total_flow_mix = float(totalflow_Ar_mix)
    except:
      totalflow_Ar_mix = None
    try:
      total_flow_mix = float(totalflow_N2_mix)
    except:
      totalflow_N2_mix = None
    o2_perc = float(O2) # Number from 0 - 100 %
    flow_o2 = (o2_perc * total_flow_mix)/100
    while flow_o2 < 0.6:
      o2_min = (0.6 * 100)/total_flow_mix
      print('O2 concentration lower than minimum {}%'.format(o2_min))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        o2_perc = float(input('Enter new concentration: '))
        flow_o2 = (o2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    while flow_o2 > 30:
      o2_max = (30 * 100)/total_flow_mix
      print('O2 concentration higher than maximum {}%'.format(o2_max))
      iterval = input('Write "Yes" for setting a new concentration or "No" for quiting the program: ')
      if iterval == 'Yes':
        o2_perc = float(input('Enter new concentration: '))
        flow_o2 = (o2_perc * total_flow_mix)/100
      elif iterval == 'No':
        raise SystemExit
    data_o2 = int(flow_o2*(32000/30))
    params_o2 = [{'node': ID_O2, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_o2}]
    status = master.write_parameters(params_o2)
    
  try:
    totalflow_He_mix = float(totalflow_He_mix) # Number in sccm
    vl.carrier_He_mix()
    totalflow_reactive = flow_co2 + flow_co + flow_ch4 + flow_h2 + flow_o2 + flow_d2
    flow_he_mix = totalflow_He_mix - totalflow_reactive
    # while flow_he_mix < 0.6:
      # print('He mixing flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # flow_he_mix = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while flow_he_mix > 60:
      print('He mixing flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_he_mix = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_he_mix = int(flow_he_mix*(32000/60))
    params_he_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                     {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_mix}]
    status = master.write_parameters(params_he_mix)
  except:
    totalflow_He_mix = None
    if Ar_mix == None and He_mix == None:
      data_he_mix = 0
      params_he_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                       {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_mix}]
      status = master.write_parameters(params_he_mix)
  
  try:
    totalflow_He_pulses = float(totalflow_He_pulses) # Number in sccm
    vl.carrier_He_pulses()
    # while totalflow_He_pulses < 0.6:
      # print('He pulses flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # totalflow_He_pulses = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while totalflow_He_pulses > 60:
      print('He pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        totalflow_He_pulses = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_he_pulses = int(totalflow_He_pulses*(32000/60))
    params_he_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_pulses}]
    status = master.write_parameters(params_he_pulses)
  except:
    totalflow_He_pulses = None
    if He_pulses == None and Ar_pulses == None:
      data_he_pulses = 0
      params_he_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_He},
                       {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_he_pulses}]
      status = master.write_parameters(params_he_pulses)
    
  
  
  try:
    totalflow_Ar_mix = float(totalflow_Ar_mix) # Number in sccm
    vl.carrier_Ar_mix()
    totalflow_reactive = flow_co2 + flow_co + flow_ch4 + flow_h2 + flow_o2 + flow_d2
    flow_ar_mix = totalflow_Ar_mix - totalflow_reactive
    # while flow_ar_mix < 0.6:
      # print('Ar mixing flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # flow_ar_mix = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while flow_ar_mix > 60:
      print('Ar mixing flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_ar_mix = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_ar_mix = int(flow_ar_mix*(32000/60))
    params_ar_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                     {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_mix}]
    status = master.write_parameters(params_ar_mix)
  except:
    totalflow_Ar_mix = None
    if Ar_mix == None and He_mix == None:
      data_ar_mix = 0
      params_ar_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                       {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_mix}]
      status = master.write_parameters(params_ar_mix)
    
  try:
    totalflow_Ar_pulses = float(totalflow_Ar_pulses) # Number in sccm
    vl.carrier_Ar_pulses()
    # while totalflow_Ar_pulses < 0.6:
      # print('Ar pulses flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # totalflow_Ar_pulses = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while totalflow_Ar_pulses > 60:
      print('Ar pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        totalflow_Ar_pulses = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_ar_pulses = int(totalflow_Ar_pulses*(32000/60))
    params_ar_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_pulses}]
    status = master.write_parameters(params_ar_pulses)
  except:
    totalflow_Ar_pulses = None
    if Ar_pulses == None and He_pulses == None:
      data_Ar_pulses = 0
      params_ar_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_Ar},
                       {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_ar_pulses}]
      status = master.write_parameters(params_ar_pulses)
    
  try:
    totalflow_N2_mix = float(totalflow_N2_mix) # Number in sccm
    totalflow_reactive = flow_co2 + flow_co + flow_ch4 + flow_h2 + flow_o2 + flow_d2
    flow_n2_mix = totalflow_N2_mix - totalflow_reactive
    # while flow_n2_mix < 0.6:
      # print('N2 mixing flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # flow_n2_mix = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while flow_n2_mix > 60:
      print('N2 mixing flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        flow_n2_mix = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_n2_mix = int(flow_n2_mix*(32000/60))
    params_n2_mix = [{'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_N2},
                     {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_n2_mix}]
    status = master.write_parameters(params_n2_mix)    
  except:
    totalflow_N2_mix = None
    
  try:
    totalflow_N2_pulses = float(totalflow_N2_pulses) # Number in sccm
    # while totalflow_N2_pulses < 0.6:
      # print('N2 pulses flow lower than minimum 0.6 sccm')
      # iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      # if iterval == 'Yes':
        # totalflow_N2_pulses = float(input('Enter new total flow: '))
      # elif iterval == 'No':
        # raise SystemExit
    while totalflow_N2_pulses > 60:
      print('N2 pulses flow higher than maximum 60 sccm')
      iterval = input('Write "Yes" for setting a new flow or "No" for quiting the program: ')
      if iterval == 'Yes':
        totalflow_N2_pulses = float(input('Enter new total flow: '))
      elif iterval == 'No':
        raise SystemExit
    data_n2_pulses = int(totalflow_N2_pulses*(32000/60))
    params_n2_pulses = [{'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8, 'data': cal_N2},
                        {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': data_n2_pulses}]
    status = master.write_parameters(params_n2_pulses)
  except:
    totalflow_N2_pulses = None
   
   
# Fuction that print the actual flows (higher than zero) passing through
# the Flow-SMS unit
def flowsms_status(self=None):
    
  # Node ID values assigned in the MFCs configuration
  ID_P_mix = 3
  ID_CO2 = 4
  ID_carrier_pulses = 5
  ID_CO = 6
  ID_carrier_mix = 7
  ID_P_pulses = 8
  ID_CH4 = 9
  ID_H2 = 10
  ID_O2 = 11  
  
  # Carrier gas ID assigned in the MFCs configuration
  carrier_mix_He = 0
  carrier_mix_Ar = 1
  carrier_mix_N2 = 2
  carrier_pulses_He = 0
  carrier_pulses_Ar = 1
  carrier_pulses_N2 = 2
  
  # Setting a delay time before reading the actual flows
  # If non present zero delay will be applied before reading
  try:
    time.sleep(self)
  except:
    self = None

  # Parameters to be read from the Flow-SMS mass flow controllers
  params_co2 = [{'node': ID_CO2, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
                {'node': ID_CO2, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_co = [{'node': ID_CO, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
               {'node': ID_CO, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_ch4 = [{'node': ID_CH4, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
                {'node': ID_CH4, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_h2 = [{'node': ID_H2, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
               {'node': ID_H2, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_o2 = [{'node': ID_O2, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
               {'node': ID_O2, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_carrier_mix = [{'node': ID_carrier_mix, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
                        {'node': ID_carrier_mix, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}, 
                        {'node': ID_carrier_mix, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8}]
  params_carrier_pulses = [{'node': ID_carrier_pulses, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
                           {'node': ID_carrier_pulses, 'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT}, 
                           {'node': ID_carrier_pulses, 'proc_nr': 1, 'parm_nr': 16, 'parm_type': propar.PP_TYPE_INT8}]
  params_p_mix = [{'node': ID_P_mix, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT}]
  params_p_pulses = [{'node': ID_P_pulses, 'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT}]

  # Sending the specified parameters to the Flow-SMS
  values_co2 = master.read_parameters(params_co2) 
  values_co = master.read_parameters(params_co)
  values_ch4 = master.read_parameters(params_ch4)
  values_h2 = master.read_parameters(params_h2)
  values_o2 = master.read_parameters(params_o2)
  values_carrier_mix = master.read_parameters(params_carrier_mix)
  values_carrier_pulses = master.read_parameters(params_carrier_pulses)
  values_p_mix = master.read_parameters(params_p_mix)
  values_p_pulses = master.read_parameters(params_p_pulses)

  # Creating induviduals lists for the read values from each MFC
  lst_co2 = []
  for value in values_co2:
    if 'data' in value:
      flow = value.get('data')
    lst_co2.append(format(flow, '.2f'))
    
  lst_co = []
  for value in values_co:
    if 'data' in value:
      flow = value.get('data')
    lst_co.append(format(flow, '.2f'))
    
  lst_ch4 = []
  for value in values_ch4:
    if 'data' in value:
      flow = value.get('data')
    lst_ch4.append(format(flow, '.2f'))
    
  lst_h2 = []
  for value in values_h2:
    if 'data' in value:
      flow = value.get('data')
    lst_h2.append(format(flow, '.2f'))
    
  lst_o2 = []
  for value in values_o2:
    if 'data' in value:
      flow = value.get('data')
    lst_o2.append(format(flow, '.2f'))
    
  lst_carrier_mix = []
  for value in values_carrier_mix:
    if 'data' in value:
      flow = value.get('data')
    lst_carrier_mix.append(format(flow, '.2f'))
  fluid_carrier_mix = float(lst_carrier_mix[2])
  if fluid_carrier_mix == 0:
    fluid_carrier_mix = 'He'
  elif fluid_carrier_mix == 1:
    fluid_carrier_mix = 'Ar'
  elif fluid_carrier_mix == 2:
    fluid_carrier_mix = 'N2'
    
  lst_carrier_pulses = []
  for value in values_carrier_pulses:
    if 'data' in value:
      flow = value.get('data')
    lst_carrier_pulses.append(format(flow, '.2f'))
  fluid_carrier_pulses = float(lst_carrier_pulses[2])
  if fluid_carrier_pulses == 0:
    fluid_carrier_pulses = 'He'
  elif fluid_carrier_pulses == 1:
    fluid_carrier_pulses = 'Ar'
  elif fluid_carrier_pulses == 2:
    fluid_carrier_pulses = 'N2'
  
  lst_p_mix = []
  for value in values_p_mix:
    if 'data' in value:
      pressure = value.get('data')
    lst_p_mix.append(format(pressure, '.2f'))  
  
  lst_p_pulses = []
  for value in values_p_pulses:
    if 'data' in value:
      pressure = value.get('data')
    lst_p_pulses.append(format(pressure, '.2f'))
  # Calculating percentage values for the actual flows
  
  
  total_flow_mix = float(format(float(lst_co[0]) + float(lst_co2[0]) + float(lst_ch4[0]) + float(lst_h2[0]) + float(lst_o2[0]) + float(lst_carrier_mix[0]), '.2f'))
  if total_flow_mix != 0:
    CO_percent = format((float(lst_co[0])/total_flow_mix)*100, '.1f')
    CO2_percent = format((float(lst_co2[0])/total_flow_mix)*100, '.1f')
    CH4_percent = format((float(lst_ch4[0])/total_flow_mix)*100, '.1f')
    H2_percent = format((float(lst_h2[0])/total_flow_mix)*100, '.1f')
    O2_percent = format((float(lst_o2[0])/total_flow_mix)*100, '.1f')
    # carrier_mix_percent = format((float(lst_carrier_mix[0])/total_flow_mix)*100, '.1f')
  
  # Creating and printing table with the actual and set flows, and line pressures
  print('------------')  
  print('Flow (sccm):')
  print('------------')
  
  if float(lst_co2[1]) == 0:
    pass
  else:
    print('CO2: meas. {}, sp. {}, {}%'.format(lst_co2[0],lst_co2[1], CO2_percent))
  
  if float(lst_ch4[1]) == 0:
    pass
  else:
    print('CH4: meas. {}, sp. {}, {}%'.format(lst_ch4[0],lst_ch4[1], CH4_percent))
  
  if float(lst_co[1]) == 0:
    pass
  else:
    print('CO:  meas. {}, sp. {}, {}%'.format(lst_co[0],lst_co[1], CO_percent))
  
  if float(lst_h2[1]) == 0:
    pass
  else:
    print('H2:  meas. {}, sp. {}, {}%'.format(lst_h2[0],lst_h2[1], H2_percent))
    
  if float(lst_o2[1]) == 0:
    pass
  else:
    print('O2:  meas. {}, sp. {}, {}%'.format(lst_o2[0],lst_o2[1], O2_percent))
    
  if float(lst_carrier_mix[1]) == 0:
    pass
  else:
    print('{} mix:    meas. {}, sp. {}'.format(fluid_carrier_mix, lst_carrier_mix[0], lst_carrier_mix[1]))
    
  if float(lst_carrier_pulses[1]) == 0:
    pass
  else:
    print('{} pulses: meas. {}, sp. {} - Carrier'.format(fluid_carrier_pulses, lst_carrier_pulses[0], lst_carrier_pulses[1]))
    
  print('Total mixing line: {} sccm'.format(total_flow_mix))
  
  print('Total pulses line: {} sccm'.format(float(lst_carrier_pulses[0])))
  
  print('----------------')
  print('Pressure (psig):')
  print('----------------')
  
  print('Pressure mixing: ' + lst_p_mix[0])
  
  print('Pressure pulses: ' + lst_p_pulses[0])
  print('/nIf using labeled gases fix the reported flows/concentrations by their correspondent calibration factor/n')  
  print('------------------------------------------------------------')
  