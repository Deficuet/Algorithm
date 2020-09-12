from PIL import Image
import os, shutil

class UnzippedConfigs:
    def __init__(self):
        self.FromPath = self.SavePath_Painting = self.SavePath_Files = ''
class ImageProcedures:
    def __init__(self, ObjDir):
        self.ObjMeshDir = ObjDir
        self.ObjBasename = os.path.basename(ObjDir)
    def GetImageBasename(self):
        self.ImgDir = Configs.FromPath + '/' + os.path.basename(self.ObjMeshDir).split('-')[0] + '.png'
        self.ImgBasename = os.path.basename(self.ImgDir)
        return self.ImgBasename
    def ImageInfo(self):
        self.DecImgBasename = os.path.basename(self.ObjMeshDir).split('-')[0] + '_dec.png'
        self.ImgName = self.ImgBasename.split('.')[0]
        ObjData = open(self.ObjMeshDir)
        self.TexPasteCordntList = []
        self.TexCropFactorList = []
        self.MaxWidth, self.MaxHeight = 0, 0
        for CordntData in ObjData.readlines():
            DataBody = CordntData.split()
            if DataBody[0] == 'v':
                POrdnt_X = abs(int(DataBody[1]))
                POrdnt_Y = int(DataBody[2])
                if POrdnt_X > self.MaxWidth: self.MaxWidth = POrdnt_X
                if POrdnt_Y > self.MaxHeight: self.MaxHeight = POrdnt_Y
                self.TexPasteCordntList.append([POrdnt_X, POrdnt_Y])
            elif DataBody[0] == 'vt': self.TexCropFactorList.append([float(DataBody[1]), float(DataBody[2])])
            else: continue
        ObjData.close()
        self.MaxWidth += 4
        self.MaxHeight += 4
        return self.MaxWidth, self.MaxHeight
    def ImagePretreat(self):
        self.EncImg = Image.open(self.ImgDir).transpose(Image.FLIP_TOP_BOTTOM)
        self.BlankPainting = Image.new('RGBA', (self.MaxWidth, self.MaxHeight), (0, 0, 0, 0))
        return int(len(self.TexPasteCordntList) / 4), self.BlankPainting
    def OrdntValue(self, Vertex, CoorSeq, FixValue): return round(float(Vertex[CoorSeq] * self.EncImg.size[CoorSeq] + FixValue))
    def ImageTreat(self, TupleNum, ImgObject):
        v1 = self.TexCropFactorList[TupleNum * 4]
        v2 = self.TexCropFactorList[TupleNum * 4 + 2]
        v1x = self.OrdntValue(v1, 0, -1)
        v1y = self.OrdntValue(v1, 1, -1)
        v2x = self.OrdntValue(v2, 0, 1)
        v2y = self.OrdntValue(v2, 1, 1)
        PasteOrdnt_X, PasteOrdnt_Y = self.TexPasteCordntList[TupleNum * 4]
        UnitImg = self.EncImg.crop((v1x, v1y, v2x, v2y))
        if PasteOrdnt_Y == 0: UnitImg = UnitImg.crop((0, 1, UnitImg.size[0], UnitImg.size[1]))
        ImgObject.paste(UnitImg, (PasteOrdnt_X, PasteOrdnt_Y))
        return ImgObject
    def FloderCheckAMove(self, floder):
        MoveTo = Configs.SavePath_Files + '/' + floder
        if not os.path.exists(MoveTo): os.mkdir(MoveTo)
        shutil.move(self.ImgDir, MoveTo + '/' + self.DecImgBasename)
        shutil.move(self.ObjMeshDir, MoveTo + '/' + self.ObjBasename)
        return 0
    def ImageFilesArchive(self, ImgObject):
        ImgObject.save(Configs.SavePath_Painting + '/' + self.DecImgBasename)
        if '_' in self.ImgName:
            CheckKW = self.ImgName.split('_')[1]
            try: CheckKW = int(CheckKW)
            except ValueError:
                if CheckKW == 'h': self.FloderCheckAMove('花嫁')
                elif CheckKW == 'g': self.FloderCheckAMove('改造')
                else: self.FloderCheckAMove('默认')
            else:
                if CheckKW > 1: self.FloderCheckAMove('换装')
                else: self.FloderCheckAMove('默认')
        else: self.FloderCheckAMove('默认')
        return 0
Configs = UnzippedConfigs()