<%@ Page Title="Chi tiết tin" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="News.aspx.cs" Inherits="AutoNewsWebsite.News" %>

<asp:Content ID="Content1" ContentPlaceHolderID="MainContent" runat="server">
    <div class="container">
        <div class="row" style="margin-top: 50px;">
            <div class="col-md-8">
                <h1 class="title" style="color: #1e598e;"><%= detailNews.Title %></h1>
                <h3 class="sapo" style="font-weight: bold; margin-top: 20px;"><%= detailNews.Description %></h3>
                <div class="news-detail">
                    <p style="margin-top: 40px; font-size: 1.2em;"><%= LoadBody() %></p>
                </div>
                <div class="clearfix"></div>
                <div class="row" style="margin-top:40px;">
                    <div class="col-md-4">
                        <asp:Button runat="server" Text="Xem bài báo gốc" ID="readFullNews" OnClick="readFullNews_Click"></asp:Button>
                    </div>
                    <div class="col-md-4"></div>
                    <div class="col-md-4"  style="text-align: right;">
                        <span>Via <a href="<%= detailNews.Url %>" target="_blank"><%= detailNews.Site %></a></span>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <h2>Tin mới nhất</h2>
                <%= GetLastestNews(10) %>
            </div>
        </div>

    </div>
</asp:Content>
