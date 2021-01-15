import csv
import json

# 'FollowerProduction[i],NetExport,NetImport,Tax,Caps
if __name__ == '__main__':
    with open('sumup.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["InstanceName", "Tax", "Trade",
                         "One_Production", "One_DomesticPrice", "One_F1_Type", "One_Production_F1", "One_F2_Type",
                         "One_Production_F2", "One_F3_Type", "One_Production_F3", "One_Import", "One_Export",
                         "One_ExportPrice", "One_Tax",
                         "Two_Production", "Two_DomesticPrice", "Two_F1_Type", "Two_Production_F1", "Two_F2_Type",
                         "Two_Production_F2", "Two_F3_Type", "Two_Production_F3", "Two_Import", "Two_Export",
                         "Two_ExportPrice", "Two_Tax"])
        for i in range(0, 50):
            for tax in [0, 1]:
                for trade in [0, 1]:
                    res = open('Instances/results/Instance_I_' + str(i) + '_Tax-' + str(tax) + '_Trade-' + str(
                        trade) + '.json')
                    ins = open('Instances/Instance_I_' + str(i) + '.json')
                    data = json.load(res)
                    insData = json.load(ins)
                    metaData = data['Meta']
                    solutionData = data['Solution']['x']

                    Countries = metaData['Countries']
                    ProdOne = solutionData[Countries[0]['FollowerStart']] + solutionData[
                        Countries[0]['FollowerStart'] + 1] + solutionData[Countries[0]['FollowerStart'] + 2]
                    ProdTwo = solutionData[Countries[1]['FollowerStart']] + solutionData[
                        Countries[1]['FollowerStart'] + 1] + solutionData[Countries[1]['FollowerStart'] + 2]
                    writer.writerow(["Instance_I_" + str(i), str(tax), str(trade),
                                     ProdOne,
                                     insData['Countries'][0]['DemandParam']['Alpha'] -
                                     insData['Countries'][0]['DemandParam']['Beta'] * (
                                                 solutionData[Countries[0]['NetImport']] - solutionData[
                                             Countries[0]['NetExport']] + ProdOne),
                                     insData['Countries'][0]['Followers']['Names'][0],
                                     solutionData[Countries[0]['FollowerStart']],
                                     insData['Countries'][0]['Followers']['Names'][1],
                                     solutionData[Countries[0]['FollowerStart'] + 1],
                                     insData['Countries'][0]['Followers']['Names'][2],
                                     solutionData[Countries[0]['FollowerStart'] + 2],
                                     solutionData[Countries[0]['NetImport']], solutionData[Countries[0]['NetExport']],
                                     solutionData[Countries[0]['ShadowPrice']],
                                     solutionData[Countries[0]['Tax']],
                                     ProdTwo,
                                     insData['Countries'][1]['DemandParam']['Alpha'] -
                                     insData['Countries'][1]['DemandParam']['Beta'] * (
                                             solutionData[Countries[1]['NetImport']] - solutionData[
                                         Countries[1]['NetExport']] + ProdTwo),
                                     insData['Countries'][1]['Followers']['Names'][0],
                                     solutionData[Countries[1]['FollowerStart']],
                                     insData['Countries'][1]['Followers']['Names'][1],
                                     solutionData[Countries[1]['FollowerStart'] + 1],
                                     insData['Countries'][1]['Followers']['Names'][2],
                                     solutionData[Countries[1]['FollowerStart'] + 2],
                                     solutionData[Countries[1]['NetImport']], solutionData[Countries[1]['NetExport']],
                                     solutionData[Countries[1]['ShadowPrice']],
                                     solutionData[Countries[1]['Tax']]])
                    res.close()
                    ins.close()
