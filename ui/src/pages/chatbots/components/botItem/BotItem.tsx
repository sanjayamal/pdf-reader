import React from "react";
import {
  CApiOutlined,
  CEditOutlined,
  CSettingOutlined,
} from "../../../../components/common/icons";
import { CAvatar, CCard, CMeta } from "../../../../components/common";
import { useNavigate } from "react-router-dom";

interface IBotItem {
  botId: string;
  name: string;
  description: string;
  profilePictureUrl: string;
}

const BotItem: React.FC<IBotItem> = ({
  botId,
  name,
  description,
  profilePictureUrl,
}) => {
  const navigate = useNavigate();
  const handleOnClick = (pathName: string) => {
    let path: string = botId;
    if (pathName.length > 0) {
      path = `${botId}/${pathName}`;
    }
    navigate(path);
  };
  return (
    <CCard
      style={{ width: "auto", marginTop: 16 }}
      actions={[
        <CSettingOutlined
          key="setting"
          onClick={() => handleOnClick("setting")}
        />,
        <CEditOutlined key="edit" onClick={() => handleOnClick("edit")} />,
        <CApiOutlined
          key="publish"
          onClick={() => {
            console.log("modal open");
          }}
        />,
      ]}
    >
      <div
        onClick={() => {
          handleOnClick("");
        }}
      >
        <CMeta
          avatar={<CAvatar src={profilePictureUrl} />}
          title={name}
          description={description}
        />
      </div>
    </CCard>
  );
};

export default BotItem;
