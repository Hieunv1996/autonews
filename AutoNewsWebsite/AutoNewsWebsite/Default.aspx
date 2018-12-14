<%@ Page Title="Trang chủ" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="AutoNewsWebsite._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">

    <div class="container">
        <asp:DataList ID="DataList1" runat="server" RepeatColumns="1">
        <ItemTemplate>
            <div class="row">
			<div class="col-md-2"></div>
			<div class="col-md-8 news">
				<a href="<%#Eval("ID", "News.aspx?ID={0}") %>" class="url-title">
					<h2 class="title"><%#Eval("Title") %></h2>
				</a>
				<h3 class="sapo"><%#Eval("Description") %></h3>
				<p class="meta">Dữ liệu thuộc <i style="color:cornflowerblue;"><a target="_blank" href="<%#Eval("Url") %>"><%#Eval("Site") %></a></i> đăng tải lúc <i><%#Eval("CreateDate") %></i></p>
			</div>
			<div class="col-md-2"></div>
		</div>
		</div>
        </ItemTemplate>
    </asp:DataList>
        <div class="row" style="text-align: center;margin-top: 20px;">
			<div class="col-md-2">
				<asp:LinkButton runat="server" ID="btnnext" OnClick="btnnext_Click" CssClass="pagging">Bài cũ hơn</asp:LinkButton>
			</div>
			<div class="col-md-8">
				<span style="text-align: center;">Trang <%= pos + 1 %>/ <%= totalPage %> Trang</span>
			</div>
			<div class="col-md-2">
				<asp:LinkButton runat="server" ID="btnprevious" OnClick="btnprevious_Click" CssClass="pagging">Bài mới hơn</asp:LinkButton>
			</div>
		</div>
    </div>

</asp:Content>
